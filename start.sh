#!/bin/bash

# Use this script for staring the main script with auto updating
# from GitHub master branch. (For this, you need to install git)
# If you don't want to auto-update, start the tool with the parameter
# 'noupdate'.
# If you want to disable update check completely after start, use
# parameter 'disable-update'. (You can re-enable it with the parameter
# 'enable-update').
# You can also rename this script to somethign like 's' or so to
# fastly start with 'sh s'.

git=true
py3=true
py=true

type git >/dev/null 2>&1 || {
    git=false
}

type python3 >/dev/null 2>&1 || {
    py3=false
}

type python >/dev/null 2>&1 || {
    py=false
}

# echo $1; exit

if [ "$1" = "disable-update" ]
then
    echo " " >> DISABLEUPDATE
fi

if [ "$1" = "enable-update" ]
then
    if [ -f DISABLEUPDATE ]
    then
        rm DISABLEUPDATE
    fi
fi

if ! $git
then
    echo "Git is not accessable!"
    echo "Can not automatically pull updated from origin repository!"
else
    if [ -f DISABLEUPDATE ]
    then
        echo "AUTO-UPDATE DISABLED!"
        echo "You can re-enable it with parameter 'enable-update'"
        echo ""
        echo "[Starting in 3 seconds...]"
        sleep 3
    else
        if [ ! "$1" = "noupdate" ]
        then
            echo "Pulling update from origin repository..."
            echo "-----------------------------------------"
            git init
            git remote add origin https://github.com/zekroTJA/serverManager.git
            git pull origin master
            echo "-----------------------------------------"
            echo "Completed updating repository."
        fi
    fi
fi

if $py3
then
    python3 src/main.py
else
    echo "No python3 version found!"
    echo "Please start this script with python3 for"
    echo "best results!"
    read -p "Do you want to start with python2 instead? (y/n): " res
    if [ "$res" = "y" ]
    then
        if $py
        then
            python src/main.py
        else
            echo "No python version installed!"
        fi
    fi
fi