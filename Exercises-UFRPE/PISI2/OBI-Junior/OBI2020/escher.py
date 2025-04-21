n = int(input("Digite quantos números tem a sequência: "))
sequencia = []
for i in range(n):
    x = int(input(f"Digite o {i}º número: "))  
    sequencia.append(x)

verificador_escher = True
# Pego uma soma aleatoria para comparar com todas as outras
# se houver ao menos uma soma diferente, ja não é escher
soma_verificadora = sequencia[0] + sequencia[-1]

for x in range(len(sequencia)):
    if sequencia[x]+ sequencia[-(x+1)] != soma_verificadora:
        verificador_escher = False
         
    
print("S") if verificador_escher else print("N")