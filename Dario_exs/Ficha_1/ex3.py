# 3. Tipo de pedido
tp=input("Insira se é uma compra ou uma venda:").strip().lower()
val=int(input("Insira o valor da compra/venda: "))

pdd = {f"tipo": tp , "valor": val} 

match pdd:
    case {"tipo": "compra", "valor": val}:
        print(f"Compra de {val}€")
    case {"tipo": "venda", "valor": val}:
        print(f"Venda de {val}€")
    case _:
        print("Pedido desconhecido")