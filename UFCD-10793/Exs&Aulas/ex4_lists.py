#Nome: Diogo Juliana
#Turma: Pipl0924
#Trabalho: Ex5 - Listas

#ex1

def imprimir_n_linhas_mesmo_numero(n):
    for i in range(1, n + 1):
        print((str(i) + " ") * i)

n = int(input("insira um número para o exercício 1: "))
imprimir_n_linhas_mesmo_numero(n)

#ex2

def imprimir_n_linhas_contagem(n):
    for i in range(1, n + 1):
        for j in range(1, i + 1):
            print(j, end=" ")
        print()

n = int(input("\n insira um número para o exercício 2: "))
imprimir_n_linhas_contagem(n)

#ex3
vetor = []

for i in range(5):
    num = int(input(f"insira o {i+1}º número inteiro: "))
    vetor.append(num)
    
print("Números lidos:", vetor)

#ex4
vetor_real = []

for i in range(10):
    num = float(input(f"Insira o {i+1}º número real: "))
    vetor_real.append(num)
    
print("Números na ordem inversa:", vetor_real[::-1])

#ex5
notas = []

for i in range(4):
    nota = float(input(f"insira a {i+1}ª nota: "))
    notas.append(nota)
media = sum(notas) / len(notas)

print("Notas:", notas)
print("Média:", media)

#ex6
caracteres = []
consoantes = []

for i in range(10):
    
    c = input(f"insira o {i+1}º caractere: ").lower()
    caracteres.append(c)
    if c.isalpha() and c not in 'aeiou':
        consoantes.append(c)
        
print("Consoantes lidas:", consoantes)
print("Total de consoantes:", len(consoantes))

#ex7
numeros = []
pares = []
impares = []

for i in range(20):
    num = int(input(f"insira o {i+1}º número: "))
    numeros.append(num)
    if num % 2 == 0:
        pares.append(num)
    else:
        impares.append(num)
        
print("Todos:", numeros)
print("Pares:", pares)
print("Ímpares:", impares)

#ex8
medias = []

for aluno in range(10):
    soma = 0
    
    for nota in range(4):
        soma += float(input(f"Aluno {aluno+1}, nota {nota+1}: "))
    media = soma / 4
    medias.append(media)

acima_de_sete = sum(1 for m in medias if m >= 7)

print("Médias:", medias)
print("Alunos com média >= 7:", acima_de_sete)

#ex9
numeros = []

for i in range(5):
    num = int(input(f"insira o {i+1}º número: "))
    numeros.append(num)
    
soma = sum(numeros)
multiplicacao = 1

for n in numeros:
    multiplicacao *= n
print("Numeros:", numeros)
print("Soma:", soma)
print("Multiplicação:", multiplicacao)

#ex10
idades = []
alturas = []

for i in range(5):
    
    idade = int(input(f"Idade da pessoa {i+1}: "))
    altura = float(input(f"Altura da pessoa {i+1} (m): "))
    idades.append(idade)
    alturas.append(altura)
    
print("Idades (inverso):", idades[::-1])
print("Alturas (inverso):", alturas[::-1])

#ex11
A = []

for i in range(10):
    A.append(int(input(f"insira o {i+1}º número de A: ")))
    
soma_quadrados = sum([x**2 for x in A])
print("Soma dos quadrados:", soma_quadrados)

#ex12
A = []
B = []

for i in range(10):
    A.append(int(input(f"A[{i+1}]: ")))
    
for i in range(10):
    B.append(int(input(f"B[{i+1}]: ")))

C = []

for i in range(10):
    C.append(A[i])
    C.append(B[i])
    
print("Vetor intercalado:", C)

#ex13
A = []
B = []
C = []

for i in range(10):
    A.append(int(input(f"A[{i+1}]: ")))
    
for i in range(10):
    B.append(int(input(f"B[{i+1}]: ")))
    
for i in range(10):
    C.append(int(input(f"C[{i+1}]: ")))

D = []
for i in range(10):
    D.extend([A[i], B[i], C[i]])
print("Vetor intercalado (3 vetores):", D)

#ex14
idades = []
alturas = []
for i in range(30):
    idade = int(input(f"Idade do aluno {i+1}: "))
    altura = float(input(f"Altura do aluno {i+1} (m): "))
    idades.append(idade)
    alturas.append(altura)

media_altura = sum(alturas) / len(alturas)
cont = 0
for i in range(30):
    if idades[i] > 13 and alturas[i] < media_altura:
        cont += 1
        
print("Media das alturas:", media_altura)
print("Alunos com mais de 13 anos e abaixo da média de altura:", cont)

#ex15

meses = ["Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho",
         "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"]

temperaturas = []

for i in range(12):
    temp = float(input(f"Temperatura média de {meses[i]}: "))
    temperaturas.append(temp)

media_anual = sum(temperaturas) / 12

print(f"Média anual: {media_anual:.2f}")

print("Meses com temperatura acima da média:")

for i in range(12):
    if temperaturas[i] > media_anual:
        print(f"{meses[i]}: {temperaturas[i]}")