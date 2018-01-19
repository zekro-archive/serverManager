 <div align="center">
     <h1>~ Server Management System ~</h1>
     <strong>A management system for servers running with screen application</strong><br><br>
     <a href="" ><img src="https://img.shields.io/badge/state-tests%20running%20in%20my%20real%20server%20envoirement-21dd9b.svg" /></a>
 </div>

 ---
This is a script where you can start screens, stop them, resume the sessions, make backups or display logs.

![](http://zekro.de/ss/ConEmu64_2018-01-06_16-15-29.png)  
*Screenshot is not up to date!*

---

## Installation

1. For best experience, you need to install:
    - [git](https://git-scm.com)
    - [Python](https://www.python.org/) *>= v.3.0*

2. Clone the repository with  
`$ git clone https://github.com/zekroTJA/serverManager.git`

3. Then cd into the repository and start the start file with  
`$ bash start.sh`

> The start file automatically updates the repository when starting.  
If you don't want to update at start, execute the script like following:  
`$ bash start.sh noupdate`  
You can also disable auto-updating completely with  
`$ bash start.sh disable-update`  
Then you can re-enable it with  
`$ bash start.sh enable-update`

---

## Commands

- **help**  
*Display a help message about all commands*<br><br>
- **start [ind/name]**  
*Start a server by index or part of the name*<br><br>
- **stop [ind/name]**  
*Stop a server by index or part of the name*<br><br>
- **resume [ind/name]**  
*Resume a server by index or part of the name*<br><br>
- **backup [ind/name]**  
*Create a backup of a server by index or part of the name in the specified backup directory*<br><br>
- **loop [ind/name]**  
*Toggles if a server should start in loop mode or not*  
*Settings are saved in `noloop.json` file*<br><br>
- **e**  
*Exit the application*<br><br>

---

## `start.sh` commands

> The `start.sh` file is a very powerfull script not just for starting the main python application, also for updating it with the github repository, checking for pip packages and checking or downloading and configuring the configuration file of the application.  
So there are some interesting commandsyou can use with this script listed below:

`USAGE: bash start.sh help`

- **help**  
*Display help message about arguments*<br><br>
- **conf** | **config**  
*Open an editor with the config.json for editing it*<br><br>
- **noupdate**  
*Start the main script without checking for updates*<br><br>
- **disable-update**  
*Permanently disable update check at start*  
*Technically it's solved by creating and checking for a file named `DISABLEUPDATE` in the scripts root directory.*<br><br>
- **enable-update**  
*Re-enable auto-updating at start*<br><br>
- **reset**  
*Reset settings for auto updating and package checking*  
*At first start, the tool will check for pip packages required and download them if needed, then it will create a file named `CHECKEDPACKAGES` to mark that they don't need to be checked at next start. This file will also be deleted with this command.*<br><br>
- **nostart**  
*With this parameter, the script will only check for updates and not start after.*  
*Actually it's just for development purpose ^^*<br><br>

---

## TODO

- [ ] Add commands
    - [x] start
    - [x] stop
    - [x] resume
    - [ ] backup
    - [ ] logs
    - [ ] *rename (?)*
    - [x] help
    - [x] exit
- [ ] Add args handling  
*Starning and stopping the server directly with start arguments of the script. For example like this:*  
`main.py start servername`
- [x] Config *(needs to be tested)*
*To set stuff like servers location, backup location...* 
