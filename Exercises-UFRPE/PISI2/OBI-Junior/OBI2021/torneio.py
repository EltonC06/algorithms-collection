resultado_partidas = []
partidas_ganhas = 0

for i in range(6):
    x = input("Resultado primeiro jogo [V/P]: ")
    resultado_partidas.append(x)
    if resultado_partidas[i] in "Vv":
        partidas_ganhas += 1

if partidas_ganhas >= 5:
    print(1)
elif partidas_ganhas >= 3:
    print(2)
elif partidas_ganhas >= 1:
    print(3)
else:
    print(-1)

