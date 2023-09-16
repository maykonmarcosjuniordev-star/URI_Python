a, b, c = (int(i) for i in input().split())
maior = (a + b + abs(a - b))//2 
maior = (maior + c + abs(maior - c))//2
print(maior, "eh o maior")
