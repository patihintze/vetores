x = int(input("Quantos números você vai digitar? "))
vet = []

for n in range(x):
    n = int(input("Digite um número: "))
    vet.append(n)

print("Números negativos: ")
for n in vet:
    if n < 0:
        print(n)