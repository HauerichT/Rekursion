def hoch(i, x=2):
    if i == 0:
        return 1
    elif i == 1:
        return x
    elif i < 0:
        return 1 / hoch(i, x)
    else:
        return x * hoch(i - 1, x)


print(hoch(i=4, x=3))

# 3*3^3
# https://www.pst.ifi.lmu.de/Lehre/fruhere-semester/wise-11-12/infoeinf/zentraluebung/zentraluebung11.pdf