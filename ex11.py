x = int(input("Quantas pessoas serão digitados? "))
alturas = []
generos = []
soma_mulheres = 0
qtd_mulheres = 0
qtd_homens = 0


for i in range(x):
    altura = float(input(f"Altura da {i+1}ª pessoa: "))
    genero = input(f"Genero da {i+1}ª pessoa: ")
    alturas.append(altura)
    generos.append(genero)
    
menor = alturas[0]
maior = 0
for i in range(x):
    if alturas[i] > maior:
        maior = alturas[i]
    if alturas[i] < menor:
        menor = alturas[i]

print(f"\nMenor altura: {menor}")
print(f"Maior altura: {maior}")

for i in range(x):
    if generos[i] == "F":
        soma_mulheres += alturas[i]
        qtd_mulheres += 1
    else: qtd_homens +=1
media_mulheres = soma_mulheres / qtd_mulheres
print(f"Media das alturas das mulheres: {media_mulheres:.2f}")
print(f"Números de homens: {qtd_homens}")