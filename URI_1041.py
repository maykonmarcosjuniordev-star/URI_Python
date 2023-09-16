mapa = ["Origem", "Q1", "Q2", "Q3", "Q4", "Eixo X", "Eixo Y"]
x, y = (float(i) for i in input().split())
cond0, cond1, cond2, cond3 = (x > 0), (y > 0), (x < 0), (y < 0)
idx = (cond0*(cond1 + 4*cond3)) + (cond2*(2*cond1 + 3*cond3))
idx += 5*((not y) and bool(x)) + 6*((not x) and bool(y))
print(mapa[idx])
