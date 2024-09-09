x = int(input("Quantos valores vai ter cada vetor? "))
vet = []
soma = 0
media = 0

for n in range(x):
    n = float(input("Digite um numero: "))
    vet.append(n)

for n in vet:
    soma += n

media = soma / x

print(f"Media do vetor: {media}")
print("Elementos abaixo da média: ")
for n in vet:
    if n < media:
        print(n)