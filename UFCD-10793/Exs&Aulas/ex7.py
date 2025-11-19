
#Nome: Diogo Juliana
#Turma: PIPL0924
#Trabalho: Ex7 - ListComp


# ============================================================
# Exercício 1 – Listas de números
# ============================================================

print("=== Exercício 1: Listas Numéricas ===")

# Lista original com 10 números inteiros
numeros = [3, -7, 0, 12, -4, 9, 5, -2, 8, -11]
print("Lista original:", numeros)

# 1. Cópia da lista original
copia = [n for n in numeros]
print("Cópia da lista:", copia)

# 2. Lista de valores positivos (>= 0)
positivos = [n for n in numeros if n >= 0]
print("Positivos:", positivos)

# 3. Lista de valores negativos (< 0)
negativos = [n for n in numeros if n < 0]
print("Negativos:", negativos)

# 4. Lista com os quadrados de todos os números
quadrados = [n**2 for n in numeros]
print("Quadrados:", quadrados)

# 5. Lista com pares e outra com ímpares
pares = [n for n in numeros if n % 2 == 0]
impares = [n for n in numeros if n % 2 != 0]
print("Pares:", pares)
print("Ímpares:", impares)

# ============================================================
# Exercício 2 – Manipulação de Frases
# ============================================================

print("\n=== Exercício 2: Manipulação de Frases ===")

frase = input("Escreve uma frase: ")

# Remover pontuação simples
for ch in [",", ".", "!", "?", ";", ":"]:
    frase = frase.replace(ch, "")

palavras = frase.split()

# 1. Lista com todas as vogais (maiúsculas e minúsculas)
vogais = [letra.lower() for letra in frase if letra.lower() in "aeiou"]
print("Vogais:", vogais)

# 2. Lista com o número de letras de cada palavra
tamanhos = [len(p) for p in palavras]
print("Tamanho de cada palavra:", tamanhos)

# 3. Lista com as palavras em minúsculas
minusculas = [p.lower() for p in palavras]
print("Palavras em minúsculas:", minusculas)

# 4. Lista com as palavras de tamanho >= 5
maiores5 = [p for p in palavras if len(p) >= 5]
print("Palavras com 5 ou mais letras:", maiores5)

# 5. Lista com a primeira letra de cada palavra
iniciais = [p[0] for p in palavras if p]
print("Primeira letra de cada palavra:", iniciais)

# 6. Lista com as palavras invertidas
invertidas = [p[::-1] for p in palavras]
print("Palavras invertidas:", invertidas)

# 7. Lista de tuplos (palavra, comprimento)
tuplos = [(p, len(p)) for p in palavras]
print("Lista de tuplos (palavra, comprimento):", tuplos)

# 8. Lista só com hashtags (sem o #)
hashtags = [p[1:] for p in palavras if p.startswith("#")]
print("Hashtags:", hashtags)

# (Bónus) Lista com as vogais únicas e ordenadas
vogais_unicas = sorted(set(vogais))
print("Vogais únicas e ordenadas:", vogais_unicas)

print("\n=== Fim do programa ===")