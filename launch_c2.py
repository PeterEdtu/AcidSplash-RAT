import sys
import server.server

acii_art = """
 @@@@@@    @@@@@@@  @@@  @@@@@@@    @@@@@@   @@@@@@@   @@@        @@@@@@    @@@@@@   @@@  @@@  
@@@@@@@@  @@@@@@@@  @@@  @@@@@@@@  @@@@@@@   @@@@@@@@  @@@       @@@@@@@@  @@@@@@@   @@@  @@@  
@@!  @@@  !@@       @@!  @@!  @@@  !@@       @@!  @@@  @@!       @@!  @@@  !@@       @@!  @@@  
!@!  @!@  !@!       !@!  !@!  @!@  !@!       !@!  @!@  !@!       !@!  @!@  !@!       !@!  @!@  
@!@!@!@!  !@!       !!@  @!@  !@!  !!@@!!    @!@@!@!   @!!       @!@!@!@!  !!@@!!    @!@!@!@!  
!!!@!!!!  !!!       !!!  !@!  !!!   !!@!!!   !!@!!!    !!!       !!!@!!!!   !!@!!!   !!!@!!!!  
!!:  !!!  :!!       !!:  !!:  !!!       !:!  !!:       !!:       !!:  !!!       !:!  !!:  !!!  
:!:  !:!  :!:       :!:  :!:  !:!      !:!   :!:        :!:      :!:  !:!      !:!   :!:  !:!  
::   :::   ::: :::   ::   :::: ::  :::: ::    ::        :: ::::  ::   :::  :::: ::   ::   :::  
 :   : :   :: :: :  :    :: :  :   :: : :     :        : :: : :   :   : :  :: : :     :   : :  
 """

version = "0.1"
official = True
author = "PeterEdtu"
github = ""

all_args = {
    "-host:x.x.x.x": "Hostname of the C2 server. Default: 127.0.0.1",
    "-port:xxxx": "Port of the C2 server. Default: 8080",
    "-debug:xxxx": "Flask server debug mode. Default: False",
    "-jitter:xxxx": "Max jitter sleep for each request (in seconds). Default: 15"
}

def main():
    print(acii_art)
    print("")
    print(f"Version: {version}")
    print(f"Author: {author}")
    print("")

    host = "127.0.0.1"
    port = 8080
    debug = False
    jitter = 15

    if len(sys.argv) > 1:
        for i, arg in enumerate(sys.argv[1:], start=1):
            try:
                if "-h" == arg or "-help" == arg:
                    print("Showing help page:")
                    for arg_k in all_args.keys():
                        print(f"{arg_k}: {all_args.get(arg_k)}")
                    return
                if "-host" in arg:
                    host = arg.split(':')[1]
                if "-port" in arg:
                    port = int(arg.split(':')[1])
                if "-jitter" in arg:
                    jitter = int(arg.split(':')[1])
                if "-debug" in arg:
                    debug_value = arg.split(':')[1]
                    if debug_value.lower() == "true":
                        debug = True
                    else:
                        debug = False
            except:
                print(f"Arg '{arg}' is not acceptable, skipping")
    
    print("")
    print(f"Setting up C2: {host}:{port} - Debug {debug} - Jitter {jitter} seconds")
    print("Launching Flask server...")
    print("======================================================================")
    print("")
    server.server.launch_server(host=host, port=port, debug=debug, jitter=jitter)

if __name__ == '__main__':
    main()