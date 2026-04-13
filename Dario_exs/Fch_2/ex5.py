# Exercício 5: 3 números em ordem crescente/decrescente ~

num1 = int(input("num1 = "))
num2 = int(input("num2 = "))
num3 = int(input("num3 = "))

list = [num1, num2, num3]
list.sort()

print(f"Crescente: {list[0]}, {list[1]}, {list[2]}")
print(f"Decrescente: {list[2]}, {list[1]}, {list[0]}\n")