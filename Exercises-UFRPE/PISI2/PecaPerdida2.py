# Input deverá receber 2 linhas
# 1ª linha: Inteiro N  (2 <= n <= 1.000)
# 2ª linha: N-1 inteiros (numerados de 1 a N) sem repetições
# Encontre o número inteiro que falta nessa sequência e retorne
# Exemplo:
# Entrada
#5
#1 2 3 5
#Saída
#4

# Notação Big O = O(n)
def lostPiece(N, sequence):
    # Haverá apenas 1 número inteiro faltando
    # Por conta disso basta somar todos os valores de uma lista hipotetica com todos os valores 
    # e diminuir da soma dos valores da lista real
    
    ideal_sum = 0
    sequence_sum = 0
    # Isso aqui é P.A (P.A Usada no lostPiece2)
    for x in range(1, N+1):
        ideal_sum += x
    
    for y in sequence:
        sequence_sum += y
    
    return ideal_sum - sequence_sum

# O(n)
def lostPiece2(N, sequence):
    # Haverá apenas 1 número inteiro faltando
    # Por conta disso basta somar todos os valores de uma lista hipotetica com todos os valores 
    # e diminuir da soma dos valores da lista real
    
    ideal_sum = 0
    sequence_sum = 0
    # Isso aqui é soma de P.A
    somaPA = (1 + N) * N // 2
    ideal_sum = somaPA
    
    for y in sequence:
        sequence_sum += y
    
    return ideal_sum - sequence_sum


n1 = 5
seq1 = [1, 2, 3, 5]
print(lostPiece2(n1, seq1))