def lampadas(N, lista):
    lampada1 = 0 # desligada
    lampada2 = 0 # desligada
    for i in lista:
        if i==2:
            lampada2 += 1
    
    lampada1 = N # independente do interruptor, seu estado será alterado
    
    if lampada1 % 2 == 0: # se for par o numero de vezes que apertou o interruptor então fica no mesmo estado que estava antes
        lampada1 = 0
    else:
        lampada1 = 1

    if lampada2 % 2 == 0:
        lampada2 = 0
    else:
        lampada2 = 1
    
    
    return [lampada1, lampada2]

print(lampadas(4, [2, 1, 2, 2]))