x = int(input("Serao digitados dados de quantos produtos? "))
nomes = []
pco_compra = []
pco_venda = []
lucro_10 = 0
lucro_10_20 = 0
lucro_20 = 0
total_compra = 0
total_venda = 0
total_lucro = 0

for i in range(x):
    print(f"Produto {i+1}: ")
    nome = input("Nome: ")
    compra = float(input("Preco de compra: "))
    venda = float(input("Preco de venda: "))
    nomes.append(nome)
    pco_compra.append(compra)
    pco_venda.append(venda)

for i in range(x):
    calculo_porc = (pco_venda[i] - pco_compra[i]) / pco_compra[i] * 100
    if calculo_porc < 10:
        lucro_10 +=1
    elif calculo_porc <= 20:
        lucro_10_20 +=1
    elif calculo_porc > 20:
        lucro_20 +=1

for i in range(x):
    total_compra += pco_compra[i]
    total_venda += pco_venda[i]
    total_lucro += pco_venda[i] - pco_compra[i]

print("\nRELATORIO:")
print(f"Lucro abaixo de 10%: {lucro_10}")
print(f"Lucro entre 10% e 20%: {lucro_10_20}")
print(f"Lucro acima de 20%: {lucro_20}")
print(f"Total de compra {total_compra:.2f}")
print(f"Total de venda {total_venda:.2f}")
print(f"Lucro total {total_lucro:.2f}")