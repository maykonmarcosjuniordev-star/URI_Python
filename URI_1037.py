mapa = ["Fora de intervalo", "Intervalo [0,25]",
        "Intervalo (25,50]", "Intervalo (50,75]",
        "Intervalo (75,100]"]
v = (float(input()))
idx = (((v % 25) != 0) + int(v//25) + (not v))
print(mapa[idx*((v >= 0) and (v <= 100))])
