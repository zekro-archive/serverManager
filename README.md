 <div align="center">
     <h1>~ Server Management System ~</h1>
     <strong>A management system for servers running with screen application</strong><br><br>
     <a href="" ><img src="https://img.shields.io/badge/state-in%20early%20development%20phase-21dd9b.svg" /></a>
 </div>

 ---
This is a script where you can start screens, stop them, resume the sessions, make backups or display logs.

![](http://zekro.de/ss/ConEmu64_2018-01-06_16-15-29.png)

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

---

## TODO

- [ ] Add commands
    - [x] start *(1)*
    - [x] stop *(1)*
    - [x] resume *(1)*
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

*(1) - Implemented, needs to be tested in a real server envoirement.*