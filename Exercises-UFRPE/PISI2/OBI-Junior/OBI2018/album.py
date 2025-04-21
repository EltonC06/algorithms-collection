'''
Entrada

A primeira linha contém um inteiro N indicando o número total de figurinhas e espaços no álbum.
A segunda linha contém um inteiro M indicando o número de figurinhas já compradas. Cada uma
das M linhas seguintes contém um número inteiro X indicando uma figurinha já comprada.

Saída

Seu programa deve produzir uma única linha contendo um inteiro representando o número de
figurinhas que falta para completar o álbum.


'''

espacos = int(input("Digite o numero total de espaços que o album possui: "))
compradas = int(input("Quantas figurinhas já foram compradas? "))
quantidade_falta = espacos
figurinhas = []

for i in range(compradas):
    x = int(input(f"Digite a numeração da {i} figurinha: "))
    repeteco = 0
    for j in figurinhas:
        if x == j:
            repeteco += 1
    
    if repeteco == 0:
        figurinhas.append(x)

print(espacos - len(figurinhas))

