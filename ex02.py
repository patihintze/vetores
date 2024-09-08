x = int(input("Quantos números você vai digitar? "))
vet = []

for n in range(x):
    n = int(input("Digite um número: "))
    vet.append(n)

soma = 0
for n in vet:
    soma += n

valores = ' '.join(str(n) for n in vet)
print(f"Valores: {valores}")
print(f"Soma: {soma}")
print(f"Media: {soma / x:.2f}")