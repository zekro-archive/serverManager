from utils import colors

c = colors.Colors

class Msgs:
    def error(cont):
        [(lambda x: 
            print(c.w.r("[ERROR] ") + x)
         )(x) for x in cont.split("\n")]