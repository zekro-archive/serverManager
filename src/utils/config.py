import json
import os
from utils.msgs import Msgs

class Config:
    def __init__(self, path):
        if not os.path.isfile(path):
            Msgs.error(
                "Config file not found!\nPlease Download the file from\n" +
                "https://github.com/zekroTJA/serverManager/blob/master/config_ex.json\n" +
                "and rename it to 'config.json'!"
            )
            exit(1)
        with open(path, "r") as f:
            raw = "".join(
                [l for l in f if not l.replace(" ", "").replace("\t", "").startswith("//")]
            )
            self.config = json.loads(raw)
    
    def get_config(self):
        return self.config