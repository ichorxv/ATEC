# Nome: Diogo Juliana
# Turma: PIPL0924
# Trabalho: Ex6 - Listas 2

#ex1

perguntas = [
    "Telefonou para a vítima?",
    "Esteve no local do crime?",
    "Mora perto da vítima?",
    "Devia para a vítima?",
    "Já trabalhou com a vítima?"
]

respostas = []

for p in perguntas:
    resposta = input(p + " (sim/não): ").strip().lower()
    respostas.append(resposta)

# Conta quantas respostas positivas
positivos = respostas.count("sim")

# Classificação
if positivos == 2:
    classificacao = "Suspeita"
elif 3 <= positivos <= 4:
    classificacao = "Cúmplice"
elif positivos == 5:
    classificacao = "Assassino"
else:
    classificacao = "Inocente"

print(f"\nClassificação: {classificacao}")

#ex2
notas = []

while True:
    valor = float(input("Digite uma nota (-1 para sair): "))
    if valor == -1:
        break
    notas.append(valor)

if len(notas) > 0:
    print("\nQuantidade de valores lidos:", len(notas))
    print("Valores informados:", notas)
    print("\nValores na ordem inversa:")
    for n in reversed(notas):
        print(n)
    
    soma = sum(notas)
    media = soma / len(notas)
    
    print(f"\nSoma dos valores: {soma}")
    print(f"Média dos valores: {media:.2f}")
    
    acima_media = len([n for n in notas if n > media])
    abaixo_sete = len([n for n in notas if n < 7])
    
    print("Quantidade de valores acima da média:", acima_media)
    print("Quantidade de valores abaixo de sete:", abaixo_sete)
else:
    print("Nenhuma nota informada.")

print("\nPrograma encerrado. Obrigado!")

#ex3
contadores = [0] * 9  # 9 faixas salariais

while True:
    vendas = input("Digite o valor das vendas brutas (-1 para sair): ")
    if vendas == "-1":
        break
    vendas = float(vendas)
    
    salario = 200 + vendas * 0.09
    indice = int((salario - 200) // 100)
    
    # Se o salário for >= 1000, vai para a última faixa
    if indice >= 8:
        indice = 8
    
    contadores[indice] += 1

# Exibe o resultado
faixas = [
    "$200 - $299", "$300 - $399", "$400 - $499", "$500 - $599",
    "$600 - $699", "$700 - $799", "$800 - $899", "$900 - $999", "$1000 ou mais"
]

print("\nDistribuição de salários:")
for i in range(9):
    print(f"{faixas[i]}: {contadores[i]} vendedor(es)")

#ex4
while True:
    nome = input("Nome do atleta (ou Enter para sair): ").strip()
    if nome == "":
        break

    saltos = []
    for i in range(5):
        salto = float(input(f"Digite o {i+1}º salto: "))
        saltos.append(salto)

    media = sum(saltos) / len(saltos)

    print(f"\nAtleta: {nome}\n")
    print("Saltos:")
    print(" - ".join(f"{s:.1f}" for s in saltos))
    print(f"\nMédia dos saltos: {media:.1f} m")
    print("-" * 40)
