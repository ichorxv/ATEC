from Pratos import *
from client_menu import *
import datetime

class Manager():
    
    def __init__(self, password, checkout, checkin, max_client):
        self.password = password
        self.checkout = checkout
        self.checkin = checkin
        self.max_client = max_client
        self.pratos = Pratos()
        self.cont = 3
        
    def gestao(self):  
        while self.cont>0:
            self.password = input("Insira a password do gestor: ")
            if self.password == "gestor": 
                self.checkin = (datetime.datetime.now())
                print(f"Data do checkin",{self.checkin.strftime("%X")})
            else:
                print(f"Tente novamente, tem mais {self.cont} tentativas")
                self.cont-=1
        self.max_client = 25
        self.pratos.listapratos
        
        
        
    
            