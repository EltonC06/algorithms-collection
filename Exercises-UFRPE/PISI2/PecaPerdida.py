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

# Primeira solução:
# Funciona apenas para listas ordenadas

# Solução ruim
def peca_perdida_1(N, sequencia):
    def insertion_sort(lista):
        for j in range(1, len(lista)):
            chave = lista[j]
            pos_vizinho = j-1
            while chave < lista[pos_vizinho] and pos_vizinho >= 0:
                lista[pos_vizinho+1] = lista[pos_vizinho]
                lista[pos_vizinho] = chave
                pos_vizinho -= 1
        
        return lista

    sequencia = insertion_sort(sequencia)
    print("Lista ordenada: ", sequencia)

    for i in range(0, N-1):
        if sequencia[i] != i+1:
            return i+1
        if i == N-2:
            return i+2
    
# Solução boa
def peca_perdida_2(N, sequencia):
    lista_clone = []
    variavel = 0
    for i in range(1, N+1):
        lista_clone.append(i)
    print(sequencia)
    print("X")
    print(lista_clone)
    for x in range(0, len(lista_clone)):
        for y in range(0, len(sequencia)):
            if lista_clone[x] == sequencia[y]:
                variavel += 1
                print(lista_clone[x], "Encontrei o ", lista_clone[x])
        # se o numero da lista clone que estou usando, não for encontrado, então o valor da variavel ficará -1 e saberei que é ele que está faltando
        variavel -= 1 
        if variavel == -1:
            return lista_clone[x]


            
# Solução mais que boa:

def peca_perdida_3(N, sequencia):
    variavel = 0
    for j in range(1, N+1):
        if j != 1:
            antecessor = j-1
            print("Verificando a existencia de ", antecessor)
            for i in sequencia:
                if i == antecessor:
                    variavel += 1
            variavel -= 1
            if variavel == -1:
                return antecessor 
    return N # se não achou o numero faltando, então com certeza o numero N que falta






n1 = 3
seq1 = [3, 1] # 2
n2 = 5
seq2 = [91, 3, 2, 5] # 4
n3 = 4
seq3 = [2, 4, 3] # 1
n4 = 7
seq4 = [1, 2, 3, 4, 5, 6] # 7


print("resposta #4: ",  peca_perdida_3(n4, seq4))

