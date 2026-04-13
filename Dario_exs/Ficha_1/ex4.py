# 4. Tipo de dado

valor = input("Introduza um valor: ")
 
#Os numeros sao todos convertidos em string mesmo sendo indicados como numeros

match valor:
 
    case str() if valor.isdigit():
 
        print(f"{valor} é um número inteiro")
 
    case str() if valor.replace('.', '', 1).isdigit() and '.' in valor:
 
        print(f"{valor} é um número decimal")
 
    case str() if valor.startswith('[') and valor.endswith(']'):
 
        print("Parece-me ser uma lista")
 
    case str():
 
        print(f"{valor} é uma string de texto comum")