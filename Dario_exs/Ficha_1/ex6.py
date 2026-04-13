# 6. Estado do servidor
stts = input("Indique o estado do servidor: ")
if( stts != "erro"):
    tmp_resp = int(input("Indique o tempo de resposta do servidor: "))
else:
    tmp_resp = 0

servidor = {"status": stts , "tempo_resposta": tmp_resp}
match servidor:
    case {"status": "ok", "tempo_resposta": tmp_resp} if tmp_resp > 200:
        print("Servidor lento")
    case {"status": "ok"}:
        print("Servidor ativo")
    case {"status": "erro"}:
        print("Servidor indisponível")
    case _:
        print("Estado desconhecido")
