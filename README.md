AcidSplash is a lightweight RAT coded in Nimlang based on simple HTTP reverse shell execution. The idea behind this project is to work on a stealthy multi-OS malware to perform EDR assessments and/or threat hunting.

Right now the project is in a 'development phase' and will change over time to add more and more MalDev principles such as payload staging, advanced obfuscation, EDR evasion techniques and persistance.

The project is composed of two elements:
- The agent "prog.nim" coded (in Nimlang)
- A really simple C2 server to distribute a commands list which the agent will acquire (in Python 3, Flask)

The commands delivered to the agent are based on a list "cmd.txt" (one per line), and can be used during realtime beaconing or pre-established commands to be sent.

Note that this project is not completed yet, and will receive a lot of changes over time when I can work on it.

![AcidSplash C2 V0.1](https://raw.githubusercontent.com/PeterEdtu/AcidSplash-RAT/main/acidsplash_c2_v0-1_example.png)

###TODO:
- Communication:
    - Change debug mode to a more stealthy method (avoid app route system)
    - AES 256 encryption
    - Key Exchange and renewal
    - Other agents
- Sandbox evasion:
    - Processes count
    - Username
    - Gather sneaky information
- Advanced Sandbox evasion with confidence score (and threshold)
    - Calculate the percentage of confidence depending on the caracteristics (C2 server)
    - Registry
- Obfuscation:
    - Strings encoding
    - Function and variables refactor
    - Payload staging
    - Commands obfuscation
    - Hidden processes alternative (curl, MSEdge)
- RAT commands:
    - Load/unload modules (in-memory commands)
    - Change settings (host, jitter, behavior)
    - Destroy agent
    - Persistance (registry, LNK etc)
    - Data Exfiltration (passwords, sensitive documents, ...)
    - Keylogger
    - Process dumping
- Dropper:
    - For Windows (HTA, DOCX, etc.)
    - For Linux (Python 2.7, etc.)
    - More things...
- C2:
    - Verify Heartbeat of agents
    - Multiple agent channels for commands (cmd.txt)
    - Real CLI interface
    - Real WebGUI interface
- UI:
    - Work on CLI
    - Work on GUI
