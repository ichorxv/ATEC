
#Nome: Diogo Juliana
#Turma: PIPL0924
#Trabalho: Ex3 - Estrutura De Repetição


# Ex1
while True:
    nota = float(input("Insira uma nota entre 0 e 10: "))
    if 0 <= nota <= 10:
        print("Nota válida:", nota)
        break
    else:
        print("Valor inválido. Tente novamente.")

# Ex2
while True:
    usuario = input("Insira o nome de usuário: ")
    senha = input("Insira a senha: ")
    if usuario != senha:
        print("log in realizado com sucesso.")
        break
    else:
        print("Erro: A senha não pode ser igual ao user. Tente novamente.")

# Ex3
while True:
    nome = input("Insira seu nome (mais de 3 caracteres): ")
    if len(nome) <= 3:
        print("Nome inválido.")
        continue

    idade = int(input("Insira sua idade (0 a 150): "))
    if not (0 <= idade <= 150):
        print("Idade inválida.")
        continue

    salario = float(input("Insira seu salário (maior que 0): "))
    if salario <= 0:
        print("Salário inválido.")
        continue

    sexo = input("Indique o seu sexo (f ou m): ").lower()
    if sexo not in ['f', 'm']:
        print("Sexo inválido.")
        continue

    estado_civil = input("Estado civil (s, c, v, d): ").lower() # solteiro/a, casado/a, viuvo/a, divorciado/a
    if estado_civil not in ['s', 'c', 'v', 'd']:
        print("Estado civil inválido.")
        continue

    print("Todos os dados foram validados com sucesso.")
    break

# Ex4
pop_a = 80000
pop_b = 200000
anos = 0

while pop_a < pop_b:
    pop_a *= 1.03
    pop_b *= 1.015
    anos += 1

print(f"Levará {anos} anos para a população do país A ultrapassar ou igualar a do país B.")

# Ex5
while True:
    try:
        pop_a = int(input("Informe a população do país A: "))
        taxa_a = float(input("Informe a taxa de crescimento de A (em %): "))
        pop_b = int(input("Informe a população do país B: "))
        taxa_b = float(input("Informe a taxa de crescimento de B (em %): "))

        if pop_a <= 0 or pop_b <= 0 or taxa_a <= 0 or taxa_b <= 0:
            print("Todos os valores devem ser maiores que zero.")
            continue

        anos = 0
        while pop_a < pop_b:
            pop_a *= 1 + (taxa_a / 100)
            pop_b *= 1 + (taxa_b / 100)
            anos += 1

        print(f"Levará {anos} anos para a população do país A ultrapassar ou igualar a do país B.")
        repetir = input("Deseja repetir? (s/n): ").lower()
        if repetir != 's':
            break
    except ValueError:
        print("Entrada inválida. Tente novamente.")

# Ex6
for i in range(1, 21):
    print(i)

# Ex6
for i in range(1, 21):
    print(i, end=' ')
print()  # Nova linha

# Ex7
maior = None
for i in range(5):
    num = float(input(f"Insira o {i+1}º numero: "))
    if maior is None or num > maior:
        maior = num
print("O maior numero é:", maior)

# Ex8
soma = 0
for i in range(5):
    num = float(input(f"Insira o {i+1}º numero: "))
    soma += num
media = soma / 5
print(f"Soma: {soma}, Média: {media}")

# Ex9
for i in range(1, 51):
    if i % 2 != 0:
        print(i, end=' ')
print()

# Ex10
inicio = int(input("Insira o primeiro numero: "))
fim = int(input("Insira o segundo numero: "))
print("Numeros no intervalo:")
for i in range(min(inicio, fim) + 1, max(inicio, fim)):
    print(i, end=' ')
print()

# Ex11
inicio = int(input("Insira o primeiro numero: "))
fim = int(input("Insira o segundo numero: "))
soma = 0
print("Numeros no intervalo:")
for i in range(min(inicio, fim) + 1, max(inicio, fim)):
    print(i, end=' ')
    soma += i
print(f"\nSoma dos numeros do intervalo: {soma}")

# Ex12
while True:
    num = int(input("Insira um numero de 1 a 10 para ver a tabuada: "))
    if 1 <= num <= 10:
        print(f"Tabuada de {num}:")
        for i in range(1, 11):
            print(f"{num} X {i} = {num * i}")
        break
    else:
        print("Numero inválido. Insira entre 1 e 10.")