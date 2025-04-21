a = int(input("Tamanho 1ª caixa: "))
b = int(input("Tamanho 2ª caixa: "))
c = int(input("Tamanho 3ª caixa: "))

qt_viagens = 0

if a == b == c:
    qt_viagens = 3
elif a == b or a == c or b == c:
    
    if a == b:
        if a + b < c:
            qt_viagens = 1
        else:
            qt_viagens = 2
    
    if a == c:
        if a + c < b:
            qt_viagens = 1
        else:
            qt_viagens = 2
    
    if b == c:
        if b + c < a:
            qt_viagens = 1
        else:
            qt_viagens = 2

else:
    qt_viagens = 1

print(qt_viagens)