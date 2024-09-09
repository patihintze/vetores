x = int(input("Quantas pessoas você vai digitar? "))
nomes = []
idades = []
maior = 0
mais_velho = ""

for i in range(x):
    print(f"Dados da {i+1}ª pessoa: ")
    nome = input("Nome: ")
    idade = int(input("Idade: "))
    nomes.append(nome)
    idades.append(idade)

for i in range(x):
    if idades[i] > maior:
        maior = idades[i]
        mais_velho = nomes[i]
print(f"Pessoa mais velha: {mais_velho}")