# 5. Análise de mensagem
msg = input("Indique a mensagem: ").strip().lower()
match msg:
    case "olá" | "bom dia":
        print("Saudação")
    case m if m.endswith("?"):
        print("Pergunta")
    case m if "tchau" in m or "adeus" in m or "xau" in m or "até já" in m or "até logo" in m:
        print("Despedida")
    case _:
        print("Mensagem generica")