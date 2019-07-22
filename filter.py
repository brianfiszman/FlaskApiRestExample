a = [1, 2, 3, 4, 5, 6]


def evenNumbers(x): return x % 2 == 0


def oddNumbers(x): return not evenNumbers(x)


print(list(filter(evenNumbers, a)))
print(list(filter(oddNumbers, a)))
