a = input()
b = list(a)
print(b)


def summ(b):
    f = 0
    for i in range(len(b)):
        f = f + int(b[i])
    print(f)


summ(b)
