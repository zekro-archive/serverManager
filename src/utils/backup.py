import shutil
import subprocess
import os
from time import gmtime, strftime


class Backup:
    def __init__(self, server, a_loc_server, a_loc_backup):
        self.loc_server = a_loc_server
        self.loc_backup = a_loc_backup
        self.server = server
        self.lastinp = ""

        while self.lastinp not in ["e", "exit", "q", "quit", "stop", "s"]:
            self.lastinp = self._print_menu()
            self._handle_cmd(self.lastinp)

    def _get_backups(self):
        if os.path.exists(self.loc_backup + "/" + self.server):
            return os.listdir(self.loc_backup + "/" + self.server)
        return []

    def _create_backup(self):
        timestamp = strftime("%Y-%m-%d_%H-%M-%S", gmtime())
        print("\nCreating backup... (This process could take a while)")
        shutil.copytree(
            self.loc_server + "/" + self.server,
            self.loc_backup + "/" + self.server + "/" + timestamp
        )

    def _restore_backup(self, ind):
        backups = list(enumerate(self._get_backups()))
        try:
            ind = int(ind) - 1
        except:
            input("Please enter a valid number as index!")
            return
        if ind in [x[0] for x in backups]:
            bu = backups[ind][1]
            print("Deleting current server save...")
            shutil.rmtree(self.loc_server + "/" + self.server)
            print("Restoring backup... (This can take a while)")
            shutil.copytree(
                self.loc_backup + "/" + self.server + "/" + bu, 
                self.loc_server + "/" + self.server
            )
            input("Reset finished!")
        else:
            input("\The entered index does not refer to a vaild backup!")
            
    def _del_backup(self, ind):
        backups = list(enumerate(self._get_backups()))
        try:
            ind = int(ind) - 1
        except:
            input("Please enter a valid number as index!")
            return
        if ind in [x[0] for x in backups]:
            bu = backups[ind][1]
            print("\nDeleting backup...")
            shutil.rmtree(self.loc_backup + "/" + self.server + "/" + bu)
        else:
            input("\The entered index does not refer to a vaild backup!")

    def _print_menu(self):
        subprocess.call('clear')
        backups = list(map(lambda x: " [%d] %s" % (x[0] + 1, x[1]), list(enumerate(self._get_backups()))))
        print(
            "\n"
            "Available backups:\n\n" +
            ("\n".join(backups) if len(backups) > 0 else " No backups available!") +
            "\n\n\nUSAGE:\n"
            "c          Create a backup at current state\n"
            "d [ind]    Delete a backup save\n"
            "r [ind]    Load a backup\n"
            "           ATTENTION: THIS WILL OVERRIDE THE CURRENT\n"
            "           SERVERS STATE!\n"
            "e          Exit this menu"
        )
        return input("> ")


    def _handle_cmd(self, cmd):

        if cmd.startswith("c"):
            self._create_backup()

        elif cmd.startswith("r"):
            args = cmd.split()
            if len(args) > 1:
                self._restore_backup(cmd.split()[1])
            else:
                input("\nUSAGE:\nreset [index]")

        elif cmd.startswith("d"):
            args = cmd.split()
            if len(args) > 1:
                self._del_backup(cmd.split()[1])
            else:
                input("\nUSAGE:\ndelete [index]")