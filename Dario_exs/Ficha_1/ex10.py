# 10. Jogo: Pedra, Papel ou Tesoura

print("Pedra, Papel ou Tesoura!!\n")
j1 = input("Escolha do jogador 1: ").strip().lower()
j2 = input("Escolha do jogador 2: ").strip().lower()
 
match (j1, j2):
    case (a, b) if a == b: # "converte" os jogadores para "a" e "b" verifica se os jogadores escolheram a mesma cosa
        print("Empate")
    case ("pedra", "tesoura") | ("tesoura", "papel") | ("papel", "pedra"):
        print("Jogador 1 venceu")
    case ("tesoura", "pedra") | ("papel", "tesoura") | ("pedra", "papel"):
        print("Jogador 2 venceu")
    case _:
        print("Jogada inválida")