# OLD V 1.x 
# https://gist.github.com/zekroTJA/2b2e10f17f5e2af3a3799efcab309061


import os
import sys
from utils import colors, msgs, system
import subprocess
import json

# getting start arguments (later essential for direct start / stpo with args)
args = sys.argv
last_inpt = ""

clr = colors.Colors
msgs = msgs.Msgs
perf = system.Sys

def clear():
    subprocess.call("clear")

def get_servers():
    """
    Returns a array of dirs wher the "run.sh" file
    exists in the directory.
    """
    out = []
    for d in os.listdir("."):
        for (path, dirs, files) in os.walk(d):
            if files and "run.sh" in files:
                out.append(d)
    return out


def is_running(server):
    """
    Returns if a server is crrently running by checking
    the path name in the 'screen -ls' std output.
    """
    proc = subprocess.Popen(["screen", "-ls"], stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    return server in str(proc.stdout.read())


def get_running_servers(servers = get_servers()):
    """
    Returns a array of all currently running servers.
    """
    return [s for s in servers if is_running(s)]


def get_start_script(server):
    """
    Returns the content of the start script ('run.sh')
    of the server.
    """
    return open(server + "/run.sh").readline()


def handle_command(cmd):
    """
    Handling commands.
    """
    invoke = cmd.split()[0]
    args = cmd.split()[1:]
    
    if invoke == "help":
        clear()
        print(
            " \n [...] - Essential argument\n"
            " ([...]) - Optional argument\n"
            " [.../...] - min. one of more arguments required\n\n"
            "   help                Display this help message\n"
            "   start [ind/name]    Start server\n"
            "   stop [ind/name]     Stop server\n"
            "   resume [ind/name]   Resume a screen session\n"
            "   backup [ind/name]   Create a backup of a server\n"
            "   logs (p)            Display log from 'screenlog.0'\n"
            "                       (p) -> Create file in apache server to display\n"
            "                              log online\n\n"
            " [Press enter to continue...]"
        )
        input()


def print_main():
    """
    Printing main GUI and returns input command.
    """
    clear()
    servers = get_servers()
    # Just for running the start message
    print(clr.w.b(
            "\n" +
            "+---------------------------------+\n"
            "| SERVER MANAGEMENT SYSTEM        |\n"
            "| Version 2.0                     |\n"
            "| (c) 2018 Ringo Hoffmann (zekro) |\n"
            "+---------------------------------+\n"
    ))

    print(perf.getSys() + "\n")

    def _pad(string):
        """
        Add spcaes after server name for formatting
        or shot them if they are over 16 chars long.
        """
        out = string
        # Max length of every server name row
        CAP = 20
        if len(string) > CAP - 4:
            return string[:CAP - 4] + "... "
        while len(out) < CAP:
            out += " "
        return out

    def _indify(inp):
        """
        If there are more than 10 servers in the list,
        the index will be transformed to [01] instead
        of defaultly [1] for example.
        """
        if len(servers) > 10:
            return "0"+ inp if inp < 10 else inp
        return inp

    def _running(s):
        """
        Returns status string for server list.
        """
        return clr.w.g("[RUNNING] ") if is_running(s) else clr.w.o("[STOPPED] ")

    ind = 0
    for s in servers:
        ind += 1
        print(
            _running(s) + clr.w.b("[%s] " % _indify(ind)) + _pad(s) + clr.w.p("['%s']" % get_start_script(s))
        )

    return input("\n\nEnter 'help' for a list of commands.\n> ")


# MAIN SECTION

while last_inpt not in ["exit", "stop", "e", "s"]:
    last_inpt = print_main()
    handle_command(last_inpt)