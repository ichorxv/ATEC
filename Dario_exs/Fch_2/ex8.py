# Exercício 8: Média de 10 notas 
notas = []

for i in range(10):
    nota = float(input(f"Nota do aluno {i+1} (0-20): "))
    notas.append(nota)

media = sum(notas) / 10
acima_igual = sum(1 for n in notas if n >= media)

print(f"Media das notas da turma: {media:.2f}")
print(f"Alunos com nota >= media: {acima_igual}")