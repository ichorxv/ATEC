class Morada:
    def __init__(self, rua, codigo_postal, porta, apt):
        self.rua = rua
        self.codigo_postal = codigo_postal
        self.porta = porta
        self.apt = apt

    def mostrar_info_m(self):
        print("INFOS:")
        print(f"Rua: {self.rua}, Porta: {self.porta}, Apt: {self.apt}, Código Postal: {self.codigo_postal}")

class Pessoa:
    def __init__(self, nome, idade, altura, morada):
        self.nome = nome
        self.idade = idade
        self.altura = altura
        self.morada = morada 

    def envelhecer(self, anos=1):

        for i in range(anos):
            self.idade += 1
            if self.idade < 25:
                self.altura += 1.5

        print(f"{self.nome} agora tem {self.idade} anos e {self.altura:.1f} cm.")

    def mostrar_info(self):
        print("INFOS:")
        print(f"Nome: {self.nome}")
        print(f"Idade: {self.idade}")
        print(f"Altura: {self.altura:.1f} cm")
        print("Morada:")
        self.morada.mostrar_info()