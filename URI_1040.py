N1, N2, N3, N4 = (float(i) for i in input().split())
M = (N1*2 + N2*3 + N3*4 + N4)/10
print("Media: %.1f" % M)
if M >= 7:
    print("Aluno aprovado.")
elif M < 5:
    print("Aluno reprovado.")
else:
    print("Aluno em exame.")
    NE = float(input())
    print("Nota do exame: %.1f" % NE)
    MF = (M + NE)/2
    if MF >= 5:
        print("Aluno aprovado.")
    else:
        print("Aluno reprovado.")
    print("Media final: %.1f" % MF)
