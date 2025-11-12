class Bola:
    def __init__(self, cor, circumferencia, material):
        
        self.cor = cor
        self.circumferencia = circumferencia
        self.material = material
        
    def trocaCor (self):
            
        cor = "branco"
        cor = input(str("Indique uma cor para a bola: (defaul: Branco)"))
            
    def mostraCor (self):
        print(f"A cor da bola é {self.cor}")

class Quadrado:
    def __init__(self, tamanho_do_lado, novo_lado):
        self.novo_lado = novo_lado
        self.tamanho_do_lado = tamanho_do_lado
        
    def MudarValorDoLado (self):
        tamanho_do_lado = self.novo_lado
            
    def RetornarValorDoLado (self):
        return self.tamanho_do_lado
            
    def CalcularArea (self):
        area = self.tamanho_do_lado*self.tamanho_do_lado
        return area
        
class Retangulo:
    def __init__(self, altura, comprimento):
        self.altura = altura
        self.comprimento = comprimento
    
    def MudarValores (self, novo_comprimento, nova_altura):
        altura = nova_altura
        comprimento = novo_comprimento
            
    def RetornarValores (self):
        return self.altura, self.comprimento
        
    def CalcularAreaPerimetro (self):
        area = self.altura * self.comprimento
        perimetro = 2*(self.altura + self.comprimento)
        
class Pessoa:
    def __init__(self,nome, idade, peso, altura):
        self.nome = nome 
        self.idade = idade
        self.peso = peso 
        self.altura = altura
        
    def Envelhecer(self):
        self.idade +=1 
        
    def Crescer (self):
        if self.idade < 21:
            self.altura + 0,5
            
    def Emagrecer (self):
        self.peso -=1
        
    def Engordar (self):
        self.peso +=1
        
class ContaCorrent:
    def __init__ (self, saldo, numero_conta, nome_correntista):
        self.saldo = saldo
        self.numero_conta = numero_conta
        self.nome_correntista = nome_correntista
    def AlternarNome(self):
        input(str("Insira o novo nome: "))
        
    def Levantamento(self):
        input(float("Insira a quantidade que deseja levantar: "))
    
    def Deposito(self):
        input(float("Insira a quantidade que deseja depositar: "))
    