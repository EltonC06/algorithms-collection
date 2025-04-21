'''
Entrada

A primeira e única linha da entrada contém um inteiro D indicando a distância do robô para o
início da quadra, em centímetros, no momento do lançamento.

Saída

Seu programa deve produzir uma única linha, contendo um inteiro, 1, 2 ou 3, indicando a pontuação
do lançamento.
'''

def basquete(D):
    if D <= 800:
        return 1
    elif D <= 1400:
        return 2
    elif D <= 2000:
        return 3
    

print(basquete(1400))