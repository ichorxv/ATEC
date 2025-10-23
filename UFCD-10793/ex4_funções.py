#Nome: Diogo Juliana
#Turma: Pipl0924
#Trabalho: Ex 4 - Funções


# EXERCiCIOS – ESTRUTURA SEQUENCIAL (Ex1)

def ex1_1():
    print("ola mundo!")

def ex1_2():
    numero = input("Insira um numero: ")
    print(f"O numero informado foi {numero}")

def ex1_3():
    num1 = float(input("Insira o primeiro numero: "))
    num2 = float(input("Insira o segundo numero: "))
    soma = num1 + num2
    print(f"A soma é: {soma}")

def ex1_4():
    nota1 = float(input("Insira a 1ª nota: "))
    nota2 = float(input("Insira a 2ª nota: "))
    nota3 = float(input("Insira a 3ª nota: "))
    nota4 = float(input("Insira a 4ª nota: "))
    media = (nota1 + nota2 + nota3 + nota4) / 4
    print(f"A média é: {media}")

def ex1_5():
    metros = float(input("Insira o valor em metros: "))
    centimetros = metros * 100
    print(f"{metros} metros equivalem a {centimetros} centimetros")

def ex1_6():
    import math
    raio = float(input("Insira o raio do circulo: "))
    area_circulo = math.pi * (raio ** 2)
    print(f"A área do circulo é: {area_circulo:.2f}")

def ex1_7():
    lado = float(input("Insira o lado do quadrado: "))
    area_quadrado = lado ** 2
    print(f"A área do quadrado é: {area_quadrado}")
    print(f"O dobro da área é: {area_quadrado * 2}")

def ex1_8():
    valor_hora = float(input("Quanto você ganha por hora? "))
    horas_mes = float(input("Quantas horas você trabalhou no mês? "))
    salario = valor_hora * horas_mes
    print(f"Seu salário neste mês é: Euros€ {salario:.2f}")

def ex1_9():
    print("Numeros impares entre 1 e 50:")
    for i in range(1, 51):
        if i % 2 != 0:
            print(i, end=" ")
    print()

def ex1_10():
    num1 = int(input("Insira o primeiro numero inteiro: "))
    num2 = int(input("Insira o segundo numero inteiro: "))
    print(f"Numeros no intervalo entre {num1} e {num2}:")
    for i in range(min(num1, num2) + 1, max(num1, num2)):
        print(i, end=" ")
    print()

def ex1_11():
    num1 = int(input("Insira o primeiro numero inteiro: "))
    num2 = int(input("Insira o segundo numero inteiro: "))
    soma = 0
    for i in range(min(num1, num2) + 1, max(num1, num2)):
        soma += i
    print(f"A soma dos numeros no intervalo entre {num1} e {num2} é: {soma}")

def ex1_12():
    numero = int(input("Insira um numero inteiro entre 1 e 10 para ver a tabuada: "))
    if 1 <= numero <= 10:
        print(f"\nTabuada de {numero}:")
        for i in range(1, 11):
            print(f"{numero} X {i} = {numero * i}")
    else:
        print("Por favor insira um numero entre 1 e 10.")

# EXERCiCIOS – ESTRUTURA DE DECISÃO (Ex2)

def ex2_1():
    num1 = float(input("Insira o primeiro numero: "))
    num2 = float(input("Insira o segundo numero: "))
    if num1 > num2:
        print(f"O maior numero é: {num1}")
    elif num2 > num1:
        print(f"O maior numero é: {num2}")
    else:
        print("Os numeros são iguais.")

def ex2_2():
    valor = float(input("Insira um valor: "))
    if valor > 0:
        print("O valor é positivo.")
    elif valor < 0:
        print("O valor é negativo.")
    else:
        print("O valor é zero.")

def ex2_3():
    sexo = input("Insira o sexo (F/M): ").strip().upper()
    if sexo == "F":
        print("F - Feminino")
    elif sexo == "M":
        print("M - Masculino")
    else:
        print("Sexo Inválido")

def ex2_4():
    letra = input("Insira uma letra: ").strip().lower()
    if letra in "aeiou":
        print("A letra é uma vogal.")
    elif letra.isalpha():
        print("A letra é uma consoante.")
    else:
        print("Caractere inválido.")

def ex2_5():
    nota1 = float(input("Insira a primeira nota: "))
    nota2 = float(input("Insira a segunda nota: "))
    media = (nota1 + nota2) / 2
    if media == 10:
        print("Aprovado com Distinção!")
    elif media >= 7:
        print("Aprovado!")
    else:
        print("Reprovado!")

def ex2_6():
    a = float(input("Insira o primeiro numero: "))
    b = float(input("Insira o segundo numero: "))
    c = float(input("Insira o terceiro numero: "))
    print(f"O maior numero é: {max(a, b, c)}")

def ex2_7():
    a = float(input("Insira o primeiro numero: "))
    b = float(input("Insira o segundo numero: "))
    c = float(input("Insira o terceiro numero: "))
    print(f"O maior numero é: {max(a, b, c)}")
    print(f"O menor numero é: {min(a, b, c)}")

def ex2_8():
    p1 = float(input("Insira o preço do primeiro produto: Euros€ "))
    p2 = float(input("Insira o preço do segundo produto: Euros€ "))
    p3 = float(input("Insira o preço do terceiro produto: Euros€ "))
    menor_preco = min(p1, p2, p3)
    print(f"deves comprar o produto que custa Euros€ {menor_preco:.2f}")

def ex2_9():
    a = float(input("Insira o primeiro numero: "))
    b = float(input("Insira o segundo numero: "))
    c = float(input("Insira o terceiro numero: "))
    nums = [a, b, c]
    nums.sort(reverse=True)
    print("Numeros em ordem decrescente:", nums)

def ex2_10():
    turno = input("Insira o turno em que estuda (M-matutino, V-vespertino, N-noturno): ").strip().upper()
    if turno == "M":
        print("Bom Dia!")
    elif turno == "V":
        print("Boa Tarde!")
    elif turno == "N":
        print("Boa Noite!")
    else:
        print("Valor Inválido!")

def ex2_11():
    salario = float(input("Insira o salário atual do colaborador: Euros€ "))
    if salario <= 280:
        percentual = 20
    elif salario <= 700:
        percentual = 15
    elif salario <= 1500:
        percentual = 10
    else:
        percentual = 5
    aumento = salario * (percentual / 100)
    novo_salario = salario + aumento
    print("\n--- Reajuste Salarial ---")
    print(f"Salario antes do reajuste: Euros€ {salario:.2f}")
    print(f"Percentual de aumento aplicado: {percentual}%")
    print(f"Valor do aumento: Euros€ {aumento:.2f}")
    print(f"Novo salario: Euros€ {novo_salario:.2f}")

# EXERCiCIOS – ESTRUTURA DE REPETIÇÃO (Ex3)

def ex3_1():
    while True:
        nota = float(input("Insira uma nota entre 0 e 10: "))
        if 0 <= nota <= 10:
            print("Nota valida!")
            break
        else:
            print("Valor invalido. Tente novamente.")

def ex3_2():
    while True:
        usuario = input("Insira o nome de usuário: ")
        senha = input("Insira a senha: ")
        if usuario != senha:
            print("Cadastro realizado com sucesso!")
            break
        else:
            print("Erro: a senha não pode ser igual ao nome de usuario. Tente novamente.")

def ex3_3():
    while True:
        nome = input("Nome: ")
        if len(nome) <= 3:
            print("Nome s ter mais de 3 caracteres.")
            continue
        idade = int(input("Idade: "))
        if not (0 <= idade <= 150):
            print("Idade s estar entre 0 e 150.")
            continue
        salario = float(input("Salario: "))
        if salario <= 0:
            print("Salario s ser maior que zero.")
            continue
        sexo = input("Sexo (f/m): ").lower()
        if sexo not in ['f', 'm']:
            print("Sexo s ser 'f' ou 'm'.")
            continue
        estado_civil = input("Estado civil (s, c, v, d): ").lower()
        if estado_civil not in ['s', 'c', 'v', 'd']:
            print("Estado civil s ser 's', 'c', 'v' ou 'd'.")
            continue
        print("Informações validas!")
        break

def ex3_4():
    popA = 80000
    popB = 200000
    anos = 0
    while popA <= popB:
        popA += popA * 0.03
        popB += popB * 0.015
        anos += 1
    print(f"Vai levar {anos} anos para o pais A ultrapassar ou igualar a população de B.")

def ex3_5():
    while True:
        popA = int(input("Informe a população do pais A: "))
        popB = int(input("Informe a população do pais B: "))
        taxaA = float(input("Informe a taxa de crescimento de A (%): "))
        taxaB = float(input("Informe a taxa de crescimento de B (%): "))
        if popA > 0 and popB > 0 and taxaA > 0 and taxaB > 0:
            anos = 0
            while popA <= popB:
                popA += popA * (taxaA / 100)
                popB += popB * (taxaB / 100)
                anos += 1
            print(f"Vai levar {anos} anos para o pais A ultrapassar ou igualar o pais B.")
        else:
            print("Valores inválidos. Tente novamente.")
        repetir = input("Deseja repetir a operação? (s/n): ").lower()
        if repetir != 's':
            break

def ex3_6():
    for i in range(1, 21):
        print(i)
    for i in range(1, 21):
        print(i, end=" ")
    print()

def ex3_7():
    maior = None
    for i in range(5):
        num = float(input(f"Insira o {i+1}º numero: "))
        if maior is None or num > maior:
            maior = num
    print("O maior numero é:", maior)

def ex3_8():
    soma = 0
    for i in range(5):
        num = float(input(f"Insira o {i+1}º numero: "))
        soma += num
    media = soma / 5
    print("Soma:", soma)
    print("Média:", media)

def ex3_9():
    for i in range(1, 51):
        if i % 2 != 0:
            print(i)

def ex3_10():
    num1 = int(input("Insira o primeiro numero: "))
    num2 = int(input("Insira o segundo numero: "))
    if num1 < num2:
        for i in range(num1 + 1, num2):
            print(i)
    else:
        for i in range(num2 + 1, num1):
            print(i)

def ex3_11():
    num1 = int(input("Insira o primeiro numero: "))
    num2 = int(input("Insira o segundo numero: "))
    soma = 0
    if num1 < num2:
        for i in range(num1 + 1, num2):
            print(i)
            soma += i
    else:
        for i in range(num2 + 1, num1):
            print(i)
            soma += i
    print("Soma dos numeros do intervalo:", soma)

def ex3_12():
    num = int(input("Insira o numero para ver a tabuada (1 a 10): "))
    print(f"Tabuada de {num}:")
    for i in range(1, 11):
        print(f"{num} X {i} = {num * i}")