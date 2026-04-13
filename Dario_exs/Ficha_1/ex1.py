# 1. Tipo de dia

dia = input("Indique o dia da semana: ").strip().lower()
 
match dia:
    case "Segunda" | "Terça" | "Terca" | "Quarta" | "Quinta" | "Sexta":
        print("Dia util!")
    case "Sábado" | "Sabado" | "Domingo":
        print("Fim de semana!")
    case _:
        print("Dia invalido...")