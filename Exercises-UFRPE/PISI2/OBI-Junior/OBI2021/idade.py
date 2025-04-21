
# Cibele > Camila and Celeste < Camila
# Camila é irmã do meio

# Coletando idade
idades = []
for x in range(3):
    idades.append(int(input(f"Digite a {x+1}ª idade: ")))

# Ordenando lista
for i in range(1, len(idades)):
    chave = idades[i]
    pos_vizinho = i-1
    while chave < idades[pos_vizinho] and pos_vizinho >= 0:
        idades[pos_vizinho+1] = idades[pos_vizinho]
        idades[pos_vizinho] = chave
        pos_vizinho -= 1

# idade do meio é a idade de Camila
print(idades[1])