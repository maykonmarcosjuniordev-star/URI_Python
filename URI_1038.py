mapa = [0, 4, 4.5, 5, 2, 1.5]
c, n = (int(i) for i in input().split())
print("Total: R$ %.2f" % (n*mapa[c]))
