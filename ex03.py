x = int(input("Quantas pessoas você vai digitar? "))
pessoas = []
idades = []
alturas = []
soma_alt = 0
media_alt = 0
menor_16 = 0
pessoa_menor_16 = []

for i in range(x):
    nome = input(f"Nome da {i+1}a pessoa: ")
    idade = int(input(f"Idade da {i+1}a pessoa: "))
    altura = float(input(f"Altura da {i+1}a pessoa: "))
    pessoas.append(nome)
    idades.append(idade)
    alturas.append(altura)

for altura in alturas:
    soma_alt += altura
print(f"Altura média: {soma_alt / x:.2f}")

for i in range(x):
    if idades[i] < 16:
        menor_16 += 1
print(f"Pessoas com menos de 16 anos: {menor_16 / x * 100:.2f}%")

for i in range(x):
    if idades[i] < 16:
        print(pessoas[i])
