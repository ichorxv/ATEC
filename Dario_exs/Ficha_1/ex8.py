# 8. Operação matemática

op = input("Tipo de conta (soma, subtracao, multiplicacao, divisao): ").strip().lower()
n1 = float(input("Número 1: "))
n2 = float(input("Número 2: "))
 
match op:
    case "soma":
        print(n1 + n2)
    case "subtracao":
        print(n1 - n2)
    case "multiplicacao":
        print(n1 * n2)
    case "divisao" if n2 != 0:
        print(n1 / n2)
    case "divisao":
        print("Erro: divisão por zero")
    case _:
        print("ERRO!!! Operação inválida!")