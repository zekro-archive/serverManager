W = "\033[0m"
R = "\033[31m"
G = "\033[32m"
O = "\033[33m"
P = "\033[35m"
B = "\033[34m"
GR = "​\033[30m"
FAT = "\033[1m"
UNDER = "\033[4m"

# https://mathias-kettner.de/lw_farbige_ausgabe_auf_der_konsole.html

class Colors:
    class p:
        def r(cont):
            print(R + cont + W)
        def g(cont):
            print(G + cont + W)
        def o(cont):
            print(O + cont + W)
        def p(cont):
            print(P + cont + W)
        def b(cont):
            print(B + cont + W)
        def gr(cont):
            print(GR + cont + W)
    class w:
        def r(cont):
            return R + cont + W
        def g(cont):
            return G + cont + W
        def o(cont):
            return O + cont + W
        def p(cont):
            return P + cont + W
        def b(cont):
            return B + cont + W
        def gr(cont):
            return GR + cont + W