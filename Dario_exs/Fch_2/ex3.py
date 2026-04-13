# Exercício 3: Ordem Crescente e Decrescente (2 números) 
num1 = int(input("num1 = "))
num2 = int(input("num2 = "))

if num1 < num2:
    print(f"Crescente: {num1}, {num2}")
    print(f"Decrescente: {num2}, {num1}")
else:
    print(f"Crescente: {num2}, {num1}")
    print(f"Decrescente: {num1}, {num2}\n")