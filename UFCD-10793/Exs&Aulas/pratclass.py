class Filme:
    def __init__(self, horaentrada, nome, minimo_idade, duracao):
        self.horaentrada = horaentrada
        self.nome = nome
        self.minimo_idade = minimo_idade
        self.duracao = duracao
        self.is_public = False


class MaquinaDoTempo:
    def __init__(self, datadestino, presente, pais, cidade):
        self.datadestino = datadestino
        self.presente = presente
        self.pais = pais
        self.cidade = cidade
        self.is_on = False
        
def start_stop(self):
    if self.is_on:
        self.is_on = False
    else:
        self.is_on = True
