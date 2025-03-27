def insertion_sort(array: list):
    for i in range(1, len(array)):
        chave = array[i]
        posicao_vizinho = i-1
        while chave < array[posicao_vizinho] and posicao_vizinho >= 0:
            array[posicao_vizinho + 1] = array[posicao_vizinho]
            array[posicao_vizinho] = chave
            
            posicao_vizinho -= 1
    
    return array


lista = [7, 6, 5, 4, 3, 2, 1]

print(insertion_sort(lista))
