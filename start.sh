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

function edit_config {
    editor="none"
    type vim >/dev/null 2>&1 && editor="vim"
    type nano >/dev/null 2>&1 && editor="nano"
    if [ ! $editor = "none" ]; then
        $editor config.json
    fi
}

function dl_config {
    wget https://raw.githubusercontent.com/zekroTJA/serverManager/master/config_ex.json -o /dev/null
    mv config_ex.json config.json
}

if [ ! -z $1 ]; then
    if [ $1 = "help" ] || [ $1 = "--help" ]; then
        echo "Usage: bash start.sh <command>"
        echo ""
        echo "  Option           Description"
        echo " --------------------------------------------------------------"
        echo "  help             Dispaly this help message"
        echo "  conf | config    Open editor with config"
        echo "  noupdate         Start without checking for update"
        echo "  disable-update   Permanently disable update check on start"
        echo "  enable-update    Re-enable auto-update at start"
        echo "  reset            Reset setting for updates and package check"
        echo "  nostart          Only update without starting src/main.py"
        echo "                   Actually for development purpose"
        echo ""
        exit
    fi

    if [ $1 = "conf" ] || [ $1 = "config" ]; then
        if [ ! -f config.json ]; then
            dl_config
        fi
        edit_config
        exit
    fi

    if [ $1 = "reset" ]; then
        rm DISABLEUPDATE >/dev/null 2>&1
        rm CHECKEDPACKAGES >/dev/null 2>&1
        echo "Reset DISABLEUPDATE and CHECKEDPACKAGES"
        exit
    fi
fi

# Testing if 'git' command works
type git >/dev/null 2>&1 || git=false

# Testing if 'python3' command works
type python3 >/dev/null 2>&1 || py3=false

# Testing if 'python' command works
type python >/dev/null 2>&1 || py=false


if $py3
then
    check_cmd="pip3"
else
    check_cmd="pip"
fi

# Checks if the required python packages are
# installed
type $check_cmd >/dev/null 2>&1 && {
    if [ ! -f CHECKEDPACKAGES ]
    then
        echo "Testing for required packages..."
        printf "  - psutil: "
        echo $(pip3 list --format=columns) | grep "psutil" --silent
        if [ ! -z $1 ]; then
            if [ $? = 1 ]
            then
                printf "will be installed... "
                $check_cmd install psutil >/dev/null
                echo "installed"
            else
                echo "installed"
            fi
        fi
        echo ""
        echo " " >> CHECKEDPACKAGES
    fi
}
    
if [ ! -z $1 ]; then
    # When 'disable-updat' parameter is given, there will be
    # created a file named 'DISABLEUPDATE' in root directory
    # of this script to signal that updated should not pulled
    # automatically on startup
    if [ "$1" = "disable-update" ]
    then
        echo " " >> DISABLEUPDATE
    fi

    # If parameter 'enable-update' is given and the file
    # 'DISABLEUPDATE' is existing, the file will be deleted
    # so that the tool will automatically pull updates from
    # origin repository
    if [ "$1" = "enable-update" ]
    then
        if [ -f DISABLEUPDATE ]
        then
            rm DISABLEUPDATE
        fi
    fi
fi

# If git is available (tested above), the tool will
# automatically update itself by pulling the lastest
# master commit from origin repository on github.
# If parameter 'noupdate' is entered or if the file
# 'DISABLEUPDATE' is existing in this direcoty, this
# steps will be skipped
if ! $git
then
    echo "Git is not accessable!"
    echo "Can not automatically pull updated from origin repository!"
else
    if [ -f DISABLEUPDATE ]
    then
        # if you want to disable the warning message, just delete this #
        # part of code.                                                #
        echo ""                                                        #
        echo "#######################################################" #
        echo "#              AUTO-UPDATE DISABLED!                  #" #
        echo "# You can re-enable it with parameter 'enable-update' #" #
        echo "#######################################################" #
        echo ""                                                        #
        echo "[Starting in 2 seconds...]"                              #
        sleep 2                                                        #
        ################################################################
    else
        if [ ! "$1" = "noupdate" ]
        then
            if [ ! -d .git ]
            then
                echo "-------------------- ATTENTION --------------------------"
                echo "This is not a cloned repository."
                echo "This folder will be deleted and cloned from repository."
                read -p "Continue? (y/n) " res
                if [ "$res" = "n" ]; then exit; fi
                echo "---------------------------------------------------------"
                echo "Cloning repository..."
                currdir=$PWD
                cd ..
                rm -r $currdir
                git clone https://github.com/zekroTJA/serverManager.git $currdir
                cd $currdir
                mv config_ex.json config.json
                edit_config
            else
                if [ ! -f config.json ] && [ -f config_ex.json ]; then
                    mv config_ex.json config.json
                    edit_config
                fi
                echo "Pulling update from origin repository..."
                echo "-----------------------------------------"
                git pull origin master
                echo "-----------------------------------------"
                echo "Completed updating repository."
            fi
        fi
    fi
fi

if [ ! -f config.json ]
then
    echo "------------------------------- ATTENTION ------------------------------------"
    echo "No 'config.json' found!"
    echo "Do you want to download the default config from:"
    echo "https://raw.githubusercontent.com/zekroTJA/serverManager/master/config_ex.json"
    read -p "(y/n) " res
    if [ "$res" = "n" ]; then
        exit 1
    fi
    dl_config
    edit_config
fi

# Now, if python3 is installed, the tool will start the main script with
# python3. Else, if python2 is installed, it will TRY starting the script
# with this version, which will - depending on the python version -
# fail with a very high probability

if [ ! -z $1 ]; then
    if [ $1 = "nostart" ]; then
        exit 1
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