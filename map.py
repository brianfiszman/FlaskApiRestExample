a, b = 1, 2
c = [a, b]


def printRes(x): return print("Hello", x)


list(map(printRes, c))
