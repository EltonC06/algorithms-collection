'''
Entrada

A primeira linha da entrada contém um inteiro M representando a idade de dona Mônica. A
segunda linha da entrada contém um inteiro A representando a idade de um dos filhos. A terceira
linha da entrada contém um inteiro B representando a idade de outro filho.

Saída

Seu programa deve imprimir uma linha, contendo um número inteiro, representando a idade do filho
mais velho de dona Mônica.
'''

idade_monica = int(input("Digite a idade de Dona Mônica: "))
A = int(input("Digite a idade do 1º filho: "))
B = int(input("Digite a idade do 2º filho: "))

idade_filho_C = idade_monica - (A+B)

idades = [A, B, idade_filho_C]

if idades[0] > idades[1] and idades[0] > idades[2]:
    print(idades[0])
elif idades[1] > idades[0] and idades[1] > idades[2]:
    print(idades[1])
else:
    print(idades[2])
