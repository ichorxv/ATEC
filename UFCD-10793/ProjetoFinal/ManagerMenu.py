import datetime
cont=3

class Manager():
    def __innit__(self, password, checkout, checkin, max_client):
        self.password = password
        self.checkout = checkout
        self.checkin = checkin
        self.max_client = max_client
        
while cont>0:
    password = input("Insira a password do gestor: ")
    if password == "gestor": 
        checkin = (datetime.datetime.now())
        print(f"Data do checkin",{checkin.strftime("%x")})
        
    else:
        print(f"Tente novamente, tem mais {cont} tentativas")
        cont=-1