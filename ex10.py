x = int(input("Quantos alunos serão digitados? "))
alunos = []
notas1 = []
notas2 = []
media = 0


for i in range(x):
    print(f"Digite nome, primeira e segunda nota do {i+1}º aluno: ")
    nome = input()
    n1 = float(input())
    n2 = float(input())
    alunos.append(nome)
    notas1.append(n1)
    notas2.append(n2)

print("Alunos aprovados: ")
for i in range(x):
    media = (notas1[i] + notas2[i]) / 2
    if media >= 6:
        print(alunos[i])