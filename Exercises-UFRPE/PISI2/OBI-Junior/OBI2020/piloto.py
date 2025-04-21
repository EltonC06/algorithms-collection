A = int(input("Digite a posição da traseira do carro A: "))
B = int(input("Digite a posição da traseira do carro B: "))
C = int(input("Digite a posição da traseira do carro C: "))


if (B-A) < (C-B):
    print("1") # acelera
elif (B-A) > (C-B):
    print("-1") # desacelera
elif (B-A) == (C-B):
    print("0") # mantém