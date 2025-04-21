n = int(input("Digite o tamanho da sequencia: "))
seq = []
contador = 0
ultimo_valor = 0

for i in range(n):
    x = int(input("Digite um valor [1 ou 2]: "))
    seq.append(x)

for j in seq: 
    if j != ultimo_valor:
        contador += 1
        ultimo_valor = j

print(contador)