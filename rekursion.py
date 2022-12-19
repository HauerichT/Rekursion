def hoch(i, x=2):
    print(str(x) + "^" + str(i))

    if i == 0:
        return 1
    elif i == 1:
        return x
    elif i < 0:
        return 1 / hoch(i, x)
    elif i > 0:
        return x * hoch(i - 1, x)


print(hoch(i=3, x=4))
