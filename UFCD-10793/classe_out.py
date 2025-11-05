class Pessoa:
    def __init__(self, nome, idade, altura, morada):
        self.nome = nome
        self.idade = idade
        self.altura = altura
        self.morada = morada 

    def envelhecer(self, anos=1):

        for _ in range(anos):
            self.idade += 1
            if self.idade < 25:
                self.altura += 1.5

        print(f"{self.nome} agora tem {self.idade} anos e {self.altura:.1f} cm.")

    def mostrar_info(self):

        print(f"Nome: {self.nome}")
        print(f"Idade: {self.idade}")
        print(f"Altura: {self.altura:.1f} cm")
        print("Morada:")
        self.morada.mostrar_info()