x = int(input("Quantos valores vai ter cada vetor? "))
vet_a = []
vet_b = []
vet_c = []
soma = 0

print("Digite os valores do vetor A: ")
for n in range(x):
    n = int(input())
    vet_a.append(n)

print("Digite os valores do vetor B: ")
for n in range(x):
    n = int(input())
    vet_b.append(n)

for i in range(x):
    soma = vet_a[i] + vet_b[i]
    vet_c.append(soma)

print(f"Vetor resultante: ")
for i in range(x):
    print(vet_c[i])