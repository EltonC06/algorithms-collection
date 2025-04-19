def parimpar(P, D1, D2):
    soma = D1+D2
    if soma % 2 == 0: # par
        if P == 0: # Alice gritou par
            return 0 # Alice ganha
        else: # Bob gritou par
            return 1 # Bob ganha
    else: # impar
        if P == 0: # Alice gritou par
            return 1
        else: # Bob gritou par
            return 0


print(parimpar(0, 1, 5))