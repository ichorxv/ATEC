# 7. Classificação de produto

cat = input("Indique o tipo de produto: ").strip().lower()
prc = int(input("Indique o preço do produto: "))

produto = {f"categoria": cat, "preço": prc}

match produto:
    case {"categoria": "eletronico", "preço": prc} if prc > 1000:
        print("Produto de luxo")
    case {"categoria": "eletronico"}:
        print("Produto comum")
    case {"categoria": "alimento"}:
        print("Produto alimentar")
    case _:
        print("Categoria desconhecida")