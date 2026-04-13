# Exercício Loop: Pares e Ímpares 
pares = impares = 0
print("Introduza 10 números:")
for i in range(10):
    num = int(input("Insira aqui: "))
    if num % 2 == 0:
        pares += 1
    else:
        impares += 1

print(f"Pares: {pares}")
print(f"Ímpares: {impares}")