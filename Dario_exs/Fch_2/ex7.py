# Exercício 7: Média Ponderada 

n1 = float(input("Nota1 (peso 2): "))
n2 = float(input("Nota2 (peso 3): "))
n3 = float(input("Nota3 (peso 5): "))

media = (n1*2 + n2*3 + n3*5) / 10

print(f"Media: {media:.1f}")
print("Aprovado" if (media >= 6) else "Reprovado")