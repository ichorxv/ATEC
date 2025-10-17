#Nome: Diogo Juliana
#Turma: Pipl0924
#Trabalho: Ex 1 - Estrutura Sequencial

#ex1
print("Ola mundo!")

#ex2
numero = input("insira um numero: ")
print(f"O numero indicado foi {numero}")

#ex3
num1 = float(input("insira o primeiro numero: "))
num2 = float(input("insira o segundo numero: "))
soma = num1 + num2
print(f"A soma é: {soma}")

#ex4
nota1 = float(input("insira a 1ª nota: "))
nota2 = float(input("insira a 2ª nota: "))
nota3 = float(input("insira a 3ª nota: "))
nota4 = float(input("insira a 4ª nota: "))
media = (nota1 + nota2 + nota3 + nota4) / 4
print(f"A media é: {media}")

#ex5
metros = float(input("insira o valor em metros: "))
centimetros = metros * 100
print(f"{metros} metros equivalem a {centimetros} centimetros")

#ex6
raio = float(input("Digite o raio do círculo: "))
area_circulo = 3.14159 * (raio ** 2)
print(f"A área do círculo é: {area_circulo}")

#ex7
lado = float(input("insira o lado do quadrado: "))
area_quadrado = lado ** 2
print(f"A área do quadrado é: {area_quadrado}")
print(f"O dobro da área é: {area_quadrado * 2}")

#ex8
valor_hora = float(input("Quanto você ganha por hora? "))
horas_mes = float(input("Quantas horas você trabalhou no mês? "))
salario = valor_hora * horas_mes
print(f"Seu salário neste mês é: R$ {salario:.2f}")

#ex9
print("Numeros ímpares entre 1 e 50:")
for i in range(1, 51):
    if i % 2 != 0:
        print(i, end=" ")
print("\n" + "-" * 40)

#ex10
num1 = int(input("insira o primeiro numero inteiro: "))
num2 = int(input("insira o segundo numero inteiro: "))

print(f"Numeros no intervalo entre {num1} e {num2}:")
for i in range(min(num1, num2) + 1, max(num1, num2)):
    print(i, end=" ")
print("\n" + "-" * 40)

#ex11
soma = 0
for i in range(min(num1, num2) + 1, max(num1, num2)):
    soma += i
print(f"A soma dos numeros no intervalo entre {num1} e {num2} é: {soma}")
print("-" * 40)

#ex12
numero = int(input("insira um numero inteiro entre 1 e 10 para verificar a tabuada: "))
if 1 <= numero <= 10:
    print(f"\nTabuada de {numero}:")
    for i in range(1, 11):
        print(f"{numero} X {i} = {numero * i}")
else:
    print("Por favor, insira um numero entre 1 e 10.")