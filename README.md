 <div align="center">
     <h1>~ Server Management System ~</h1>
     <strong>A management system for servers running with screen application</strong><br><br>
     <a href="" ><img src="https://img.shields.io/badge/state-tests%20running%20in%20my%20real%20server%20envoirement-21dd9b.svg" /></a>
 </div>

 ---
This is a script where you can start screens, stop them, resume the sessions, make backups or display logs.

![](https://zekro.de/src/servermanagementsystem_c39_screen.png)  
*Screenshot topicality: Commit #39*

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

### Permissions

> For following commands we assume that the ServerManagers install location is ***/serverManager*** and the server accounts name is ***server***.

There could be some problems with missing permissions.
First of all, be sure, that the user, you are starting the ServerManager with, has full permissions to the directory, the ServerManager is running in. Else, you could get an exception like this:
```
Traceback (most recent call last):
  File "src/main.py", line 302, in <module>
    handle_command(last_inpt, servers)
  File "src/main.py", line 135, in handle_command
    tmstmp.set_timestamp(server)
  File "/serverManager/src/utils/tmstmp.py", line 15, in set_timestamp
    with open("%s/%s/STARTTIME" % (conf["dirs"]["servers"], server), "w") as fw:
PermissionError: [Errno 13] Permission denied: '/*yourserverloc*/STARTTIME'
````

You can check folder permissions with the following commands:
```
$ cd /serverManager
$ ls -lisah
```

Then it should look like this:
```
total 444K
97260575 4.0K drwxrwxrwx  4 server root   4.0K Jan 25 08:33 .
95552298 4.0K drwxr-xr-x 29 root   root   4.0K Jan 18 11:06 ..
97259970 4.0K -rw-------  1 server server  173 Jan 25 08:33 .bash_history
97260576 4.0K drwxr-xr-x  8 server root   4.0K Jan 25 08:36 .git
97260615 4.0K -rw-r--r--  1 server root     66 Jan 18 11:06 .gitattributes
97260616 4.0K -rw-r--r--  1 server root     94 Jan 18 11:06 .gitignore
97260635 4.0K -rw-r--r--  1 server root     10 Jan 18 15:42 CHECKEDPACKAGES
97260617 4.0K -rw-r--r--  1 server root   1.6K Jan 18 11:06 README.md
97260627 4.0K -rw-r--r--  1 server root    847 Jan 18 13:57 config.json
97260632 4.0K -rw-r--r--  1 server root     13 Jan 19 08:10 noloop.json
97260647 384K -rw-r--r--  1 server root   377K Jan 25 08:23 screenlog.0
97260619 4.0K drwxr-xr-x  4 server root   4.0K Jan 20 12:01 src
97260618 8.0K -rw-r--r--  1 server root   7.2K Jan 18 15:43 start
97260646 8.0K -rw-r--r--  1 server root   7.2K Jan 19 07:23 start.sh
```

Else, you can get permissions with entering following command as **root**:
```
$ chown -R server /serverManager
# Parameter "-R" will execute own rights recoursively
```

If you get errors like this:

![](https://zekro.de/src/servermanager_screen_noperms.png)

Then you may need to grant execution permissions to the **`runner.sh`** file:  
*This command needs also be executed as **root**.*
```
$ chmod +x /serverManager/src/runner.sh
```

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
- **restart [ind/name]**  
*Restarts a server by index or name*<br><br>
- **backup [ind/name]**  
*Create a backup of a server by index or part of the name in the specified backup directory, restore or delete a backup*<br><br>
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
    - [x] backup
    - [ ] logs *(?)*  
    *This seems more problematic as I thought before, because thre running screen process refers to the root location of the `runner.sh` file while writing the `screenlog.0`, which I wanted to dispaly here. So every running server is inserting their logs into the same `screenlog.0` file so it's senseless to display it. Maybe there is a special parameter for screen to change this?*
    - [ ] *rename (?)*
    - [x] help
    - [x] exit
- [ ] Add args handling  
*Starning and stopping the server directly with start arguments of the script. For example like this:*  
`main.py start servername`
- [x] Config *(needs to be tested)*
*To set stuff like servers location, backup location...*
- [x] "Running since" display 
*So you can see in the main screen how long the servers are runnuing after last (re-)start*
