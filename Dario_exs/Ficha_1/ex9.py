# 9. Processamento de requisição

meth=input("Indique o metodo de processamento: ").strip().upper()

if(meth == "POST"):
    content = input("Indique os conteudos: ")
else:
    content= ""

req = {f"metodo": meth, "conteudo": content}

match req:
    case {"metodo": "GET"}:
        print("Requisição GET recebida")
    case {"metodo": "POST", "conteudo": ""} | {"metodo": "POST", "conteudo": None}:
        print("Requisição POST sem dados")
    case {"metodo": "POST", "conteudo": content}:
        print("Requisição POST com dados válidos")
    case _:
        print("Método não suportado")