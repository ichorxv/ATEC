#



import datetime
from Pratos import *

cont=3

class Manager():
    
    def __innit__(self, password, checkout, checkin, max_client):
        self.password = password
        self.checkout = checkout
        self.checkin = checkin
        self.max_client = max_client
        self.pratos = Pratos()
        
    def gestao(self):  
        while cont>0:
            self.password = input("Insira a password do gestor: ")
            if self.password == "gestor": 
                self.checkin = (datetime.datetime.now())
                print(f"Data do checkin",{self.checkin.strftime("%X")})
            else:
                print(f"Tente novamente, tem mais {cont} tentativas")
                cont-=1
        self.max_client = 25
        self.pratos.listapratos
        
        
        
    
            