CronOS
================

## Table of Contents
- [OS.py](#os.py)
- [Commands](#commands)
- [Director](#Directory)
- [package Creation Tool](#Pkgs)


## [OS.py](./OS.py)
Main Python File

OS.py is the file that you run 

default loggin is ```guest``` wilth password of ```1234```

go to ```Drive/System/users.json``` to change users

and register command comeing soon

=================



## Commands

```
-run 
```
(program name ending in .py)

```
programs 
```
(list all installed programs)

```
scan()  
```
(scan for viruses)

```
whoami
```
(tells you who you are logged in as)

```
exit()
```
(exit OS window)

```
rom 
```
(will be changed to dir, lists root files)

```
clear
```
(clears term)

```
logout
```
(logs you out)

```
cd 
```
(brings you to cd) Work In Progress




## Directory

```
Cron-OS
├─ .gitignore
├─ Drive
│  ├─ ProgramFiles
│  │  ├─ compute.py
│  │  ├─ joke.py
│  │  └─ main.py
│  └─ System
│     ├─ AntiV.py
│     ├─ Backups
│     │  └─ code.av
│     ├─ color.py
│     ├─ data
│     │  ├─ Logo1.png
│     │  └─ Logo2.png
│     ├─ help.txt
│     ├─ load.py
│     ├─ Misc
│     │  └─ Sys_info.json
│     ├─ packages.py
│     ├─ pkg
│     │  ├─ pkg.py
│     │  └─ __pycache__
│     │     ├─ pkg.cpython-38.pyc
│     │     └─ pkg.cpython-39.pyc
│     ├─ users.json
│     └─ __pycache__
│        ├─ color.cpython-39.pyc
│        ├─ load.cpython-39.pyc
│        ├─ packages.cpython-38.pyc
│        └─ packages.cpython-39.pyc
├─ OS.py
└─ readme.md

```


## Pkgs

```
class pkgs:  
  def run(cmd):
    
    try:
      command_1 = cmd.split()[0]
      try:
        command_2 = cmd.split()[1]
      except:
        pass
    except:
      pass
    
    
    
    ## >> insert package here <<

```

put this code in a file names ```pkg.py``` in ```Drive/System/pkg/(pkg.py)``` replace pkg.py

return 11 to logout and return 1 to make it so OS.py doesent throw an error


