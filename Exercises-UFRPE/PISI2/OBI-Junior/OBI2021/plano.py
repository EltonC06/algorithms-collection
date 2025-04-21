quota = int(input("Digite o valor da quota mensal em mb: "))
meses = int(input("Digite o número de meses: "))

megabytes_mensal = []
megabytes_total = quota * meses
megabytes_gasto = 0

for x in range(meses):
    megabytes_mensal.append(int(input(f"Digite o mb gasto no mês {x+1}: ")))
    megabytes_gasto += megabytes_mensal[x]

# +quota do mês seguinte 
print((megabytes_total+quota) - megabytes_gasto)
