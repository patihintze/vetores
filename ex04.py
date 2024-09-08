x = int(input("Quantos números você vai digitar? "))
vet = []
qtd_pares = 0

for n in range(x):
    n = int(input("Digite um número: "))
    vet.append(n)

print("Números pares:")
for n in vet:
    if n % 2 == 0:
        print(n, end=" ")
        qtd_pares += 1

print(f"\nQuantidade de pares: {qtd_pares}")