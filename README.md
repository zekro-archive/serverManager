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
`$ sh start.sh`

> The start file automatically updates the repository when starting.  
If you don't want to update at start, execute the script like following:  
`$ sh start.sh noupdate`  
You can also disable auto-updating completely with  
`$ sh start.sh disable-update`  
Then you can re-enable it with  
`$ sh start.sh enable-update`

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
- [ ] Config  
*To set stuff like servers location, backup location...* 