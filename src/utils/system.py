import psutil
from utils import colors

c = colors.Colors

class Sys:
    def getSys():
        cpulaod = psutil.cpu_percent()
        mem = psutil.virtual_memory()
        memtotal = mem.total / 1024 / 1024
        memused = mem.used / 1024 / 1024
        memload = mem.percent
        disk = psutil.disk_usage(".")
        disktotal = disk.total / 1024 / 1024 / 1024
        diskused = disk.used / 1024 / 1024 / 1024
        diskload = disk.percent

        def _getBar(val):
            if val < 33:
                return c.w.g("||||||||||||||||||||"[:int(20 * val / 100)])
            elif val < 75:
                return c.w.o("||||||||||||||||||||"[:int(20 * val / 100)])
            else:
                return c.w.r("||||||||||||||||||||"[:int(20 * val / 100)])

        def _getSpace(val):
            return "                    "[:20 - int((20 * val / 100))]

        return str(
            """
  CPU:    [%s%s] %d %%
  RAM:    [%s%s] %d %%
  Space:  [%s%s] %d %%
            """ % (
                _getBar(cpulaod),
                _getSpace(cpulaod),
                cpulaod,
                _getBar(memload),
                _getSpace(memload),
                memload,
                _getBar(diskload),
                _getSpace(diskload),
                diskload
            )
        )

        # return str("CPU load:        %d %%\n"
        #            "Memory (used):   %d MiB / %d MiB (%d %%)\n"
        #            "Space (used):    %d GiB / %d GiB (%d %%)"
        #            % (cpulaod, memused, memtotal, memload, diskused, disktotal, diskload))