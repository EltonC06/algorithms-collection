# soma dos elementos de um array
def vector_sum(array, itens):
    if itens == 0:  # se eu quero somar apenas o 1º item....
        return array[0]  # retorna o 1º item
    else:
        return array[itens] + vector_sum(array, itens-1)


arr = [2, 1, 3, 4, 5]
print(vector_sum(arr, 4))