x = int(input("Quantos números você vai digitar? "))
vet = []
soma = 0
qtd_pares = 0

for n in range(x):
    n = int(input("Digite um numero: "))
    vet.append(n)

for n in vet:
    if n % 2 == 0:
        soma += n
        qtd_pares += 1

if soma != 0:
    media = soma / qtd_pares
    print(f"Média dos pares: {media}")
else: print("Nenhum número par.")
    