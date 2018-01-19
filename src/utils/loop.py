import os
import json


class Loop:
    def __init__(self):
        if os.path.isfile("noloop.json"):
            with open("noloop.json", "r") as f:
                cont = f.read()
                self.conf = json.loads(cont)
        else:
            self.conf = {}

    def get_c(self):
        return self.conf

    def set_c(self, cconf):
        self.conf = cconf
        with open("noloop.json", "w") as fw:
            fw.write(json.dumps(cconf))