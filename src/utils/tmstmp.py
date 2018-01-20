from datetime import datetime
from os import path
import time

# [       ]
# [ERROR  ]
# [0004:12]

# 1h =  3600s
# 1d = 86400s

conf = None

def set_timestamp(server):
    with open("%s/%s/STARTTIME" % (conf["dirs"]["servers"], server), "w") as fw:
        fw.write(str(time.time()))


def get_timestamp(server):
    def _pad(s, l):
        out = str(int(s))
        while len(out) < l:
            out = "0" + out
        return out

    if path.isfile("%s/%s/STARTTIME" % (conf["dirs"]["servers"], server)):
        with open("%s/%s/STARTTIME" % (conf["dirs"]["servers"], server), "r") as f:
            starttime = float(f.read())
            delay = time.time() - starttime
            d = delay / 86400
            h = delay % 86400 / 3600
            return "%s:%s" % (_pad(d, 4), _pad(h, 2))
    else:
        return None