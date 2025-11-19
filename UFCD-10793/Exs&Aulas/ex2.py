#Nome: Diogo Juliana
#Turma: PIPL0924
#Trabalho: Ex 2 - Estrutura De Decisão

#ex1
num1 = float(input("Insira o primeiro numeros "))
num2 = float(input("Insira o segundo numeros "))

if num1 > num2:
    print(f"O maior numerosé: {num1}")
elif num2 > num1:
    print(f"O maior numerosé: {num2}")
else:
    print("Os numeros são iguais.")

print("-" * 10)

#ex2
valor = float(input("Insira um valor: "))
if valor > 0:
    print("O valor é positivo.")
elif valor < 0:
    print("O valor é negativo.")
else:
    print("O valor é zero.")

print("-" * 10)

#ex3
sexo = input("Insira o sexo (F/M): ").strip().upper()
if sexo == "F":
    print("F - Feminino")
elif sexo == "M":
    print("M - Masculino")
else:
    print("Sexo Invalido")

print("-" * 10)

#ex1
letra = input("Insira uma letra: ").strip().lower()
if letra in "aeiou":
    print("A letra é uma vogal.")
elif letra.isalpha():
    print("A letra é uma consoante.")
else:
    print("Caractere invalido.")

print("-" * 10)

#ex5
nota1 = float(input("Insira a primeira nota: "))
nota2 = float(input("Insira a segunda nota: "))
media = (nota1 + nota2) / 2

if media == 10:
    print("Aprovado com Distinção!")
elif media >= 7:
    print("Aprovado!")
else:
    print("Reprovado!")

print("-" * 10)

#ex6
a = float(input("Insira o primeiro numeros "))
b = float(input("Insira o segundo numeros "))
c = float(input("Insira o terceiro numeros "))
print(f"O maior numerosé: {max(a, b, c)}")

print("-" * 10)

#ex7
print(f"O maior numero é: {max(a, b, c)}")
print(f"O menor numero é: {min(a, b, c)}")

print("-" * 10)

#ex8
p1 = float(input("Insira o preço do primeiro produto: € "))
p2 = float(input("Insira o preço do segundo produto: € "))
p3 = float(input("Insira o preço do terceiro produto: € "))

menor_preco = min(p1, p2, p3)
print(f"Deverá comprar o produto que custa € {menor_preco:.2f}")

print("-" * 10)

#ex9
nums = [a, b, c]
nums.sort(reverse=True)
print("numeros em ordem decrescente:", nums)

print("-" * 10)

#ex10
turno = input("Insira o turno em que estuda (M-matutino, V-vespertino, N-noturno): ").strip().upper()
if turno == "M":
    print("Bom Dia!")
elif turno == "V":
    print("Boa Tarde!")
elif turno == "N":
    print("Boa Noite!")
else:
    print("Valor Invalido!")

print("-" * 10)

#ex11
salario = float(input("Insira o salario atual do colaborador: € "))

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
print(f"Salario antes do reajuste: € {salario:.2f}")
print(f"Percentual de aumento aplicado: {percentual}%")
print(f"Valor do aumento: € {aumento:.2f}")
print(f"Novo salario: € {novo_salario:.2f}")
print("-" * 10)