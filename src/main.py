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


def handle_command(cmd, servers):
    """
    Handling commands.
    """
    if not servers:
        servers = get_servers()
    if len(cmd) == 0:
        return
    invoke = cmd.split()[0]
    args = cmd.split()[1:]

    def _select(args):
        args_s = " ".join(args).lower().replace(" noloop", "")
        try:
            ind = int(args[0]) - 1
            if ind > len(servers) or ind < 0:
                return None
            return servers[ind]
        except:
            for s in servers:
                if args_s in s.lower():
                    return s
            return None

    # Help command
    if invoke == "help":
        clear()
        input(
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
            "                              log online\n"
            "   e                   Exit tool\n"
            "   <Enter>             If you just press enter the list will refresh\n\n"
            " [Press enter to continue...]\n\n"
        )

    # Start command
    elif invoke == "start":
        if len(args) == 0:
             input("USAGE: start [ind/name]\n")
             return
        noloop = "noloop" in args
        server = _select(args)
        if not server:
            input(clr.w.r("[ERROR] ") + "Can not find server '%s'..." % (" ".join(args)))
        elif is_running(server):
            input(clr.w.r("[ERROR] ") + "You can not start a still running server...")
        elif not get_start_script(server):
            input(clr.w.r("[ERROR] ") + "The start script of the server is empty...")
        else:
            try:
                subprocess.call(["screen", "-S", server, "-L", "sh", "src/runner.sh", get_start_script(server), server, "noloop" if noloop else ""])
            except Exception as e:
                input(clr.w.r("[ERROR] ") + "An unexpected error occured while starting:\n" + e)

    # Stop command
    elif invoke == "stop":
        if len(args) == 0:
            input("USAGE: stop [ind/name]\n")
            return
        server = _select(args)
        if not server:
            input(clr.w.r("[ERROR] ") + "Can not find server '%s'..." % (" ".join(args)))
        if not is_running(server):
            input(clr.w.r("[ERROR] ") + "You can not stop a not running server...")
        else:
            try:
                subprocess.call(["screen", "-X", "-S", server, "quit"])
            except Exception as e:
                input(clr.w.r("[ERROR] ") + "An unexpected error occured while stopping:\n" + e)

    # Resume command
    elif invoke == "resume":
        if len(args) == 0:
            input("USAGE: resume [ind/name]\n")
            return
        server = _select(args)
        if not server:
            input(clr.w.r("[ERROR] ") + "Can not find server '%s'..." % (" ".join(args)))
        if not is_running(server):
            input(clr.w.r("[ERROR] ") + "You can not resume a stopped server...")
        else:
            try:
                subprocess.call(["screen", "-r", server])
            except Exception as e:
                input(clr.w.r("[ERROR] ") + "An unexpected error occured while resuming:\n" + e)


def print_main(servers):
    """
    Printing main GUI and returns input command.
    """
    clear()
    if not servers:
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

    def _cut(string, cap):
        if len(string) > cap:
            return string[:cap - 3] + "..."
        return string

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
            _running(s) + clr.w.b("[%s] " % _indify(ind)) + _pad(s) + clr.w.p("['%s']" % _cut(get_start_script(s).replace("\n", ""), 35))
        )

    return input("\n\nEnter 'help' for a list of commands.\n> ")


# MAIN SECTION

while last_inpt not in ["exit", "stop", "e", "s"]:
    servers = get_servers()
    last_inpt = print_main(servers)
    handle_command(last_inpt, servers)