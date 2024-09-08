x = int(input("Quantos números você vai digitar? "))
vet = []
maior_numero = 0
pos_maior = 0

for n in range(x):
    n = int(input("Digite um número: "))
    vet.append(n)

for n in range(len(vet)):
    if vet[n] > maior_numero:
        maior_numero = vet[n]
        pos_maior = n

print(f"Maior valor: {maior_numero}")
print(f"Posição do maior valor: {pos_maior}")