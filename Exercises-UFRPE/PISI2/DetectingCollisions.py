def verificador_colisao_2D(A1, A2, B1, B2):
    if B2 < A1 or B1 > A2:
        if B2 < A1 and B1 > A2:
            return True
        else:
            return False
    else:
        return True


retA = []
retB = []
retA = input("Digite os valores do Retangulo A [x0, y0, x1, y1]: ").split(" ")
retB = input("Digite os valores do Retangulo B [x0, y0, x1, y1]: ").split(" ")


# verificando colisão eixo X:
if verificador_colisao_2D(retA[0], retA[2], retB[0], retB[2]):
    # Colidiu horizontalmente, verificando colisão eixo Y
    if verificador_colisao_2D(retA[1], retA[3], retB[1], retB[3]):
        #Colidiu
        print("1")
    else:
        # Não colidiu
        print("0")
else:
    # Não colidu
    print("0")