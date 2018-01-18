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
    echo "Testing for required packages..."
    printf "  - psutil: "
    echo $(pip3 list --format=columns) | grep "psutil" --silent
    if [ $? = 1 ]
    then
        printf "will be installed... "
        $check_cmd install psutil >/dev/null
        echo "installed"
    else
        echo "installed"
    fi
    echo ""
}


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
        echo "[Starting in 3 seconds...]"                              #
        sleep 3                                                        #
        ################################################################
    else
        if [ ! "$1" = "noupdate" ]
        then
            if [ ! -d .git ]
            then
                echo "------------------------ ATTENTION ------------------------------"
                echo "This is not a cloned repository."
                echo "This folder will be deleted and cloned from repository."
                read -p "Continue? (y/n)" res
                if [ "$res" = "n" ]; then exit; fi
                echo "-----------------------------------------------------------------"
                echo "Cloning repository..."
                currdir=$PWD
                cd ..
                rm -r $currdir
                git clone https://github.com/zekroTJA/serverManager.git $currdir
                cd $currdir
                mv config_ex.json config.json
            else
                if [ ! -f config.json ] && [ -f config_ex.json ]; then
                    mv config_ex.json config.json
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

# Now, if python3 is installed, the tool will start the main script with
# python3. Else, if python2 is installed, it will TRY starting the script
# with this version, which will - depending on the python version -
# fail with a very high probability

if [ $1 = "nostart" ]; then
    exit 1
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