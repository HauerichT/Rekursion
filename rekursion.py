def hoch(*args):
    if len(args) == 0:
        return print("Keine Argumente übergeben!")
    elif len(args) == 1:
        x = 2
        i = args[0]
    else:
        x = args[0]
        i = args[1]

    if i == 0:
        return 1
    elif i == 1:
        return x
    elif i < 0:
        return 1 / hoch(x, -i)
    elif i > 0:
        return x * hoch(x, i - 1)


print(hoch(4, 3))
