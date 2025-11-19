#grupo: Daniel Barateiro, Diogo Juliana, Luis Ferreira
#turma: PI0924
#Menu de cliente para o projeto final
#---------------------------------------------------------
from Pratos import *
from Reservas import *
opc=""
class Client():
  def __init__(self, menu_restaurante):
    self.menu_restaurante = menu_restaurante
    self.reserva = reservas()
    self.pratos = Pratos()
  def menu_clientes(self):
      opc=input("Bem vindo ao restaurante jatfuioku\nIndique a opção desejada:\n(1)Consultar o menu\n(2)Agendar uma reserva\n(3)Pedir pratos\n(4)Sair\n")
      match opc:
        case "1":
          self.pratos.listapratos()
        case "2":
            self.horario=input("Qual horario deseja fazer a sua reserva?(1)Dia;(2)Noite\n")
            if self.horario == "1":
              self.reserva.horalmoco()
            elif self.horario == "2":
              self.reserva.horajantar()
        case "3":
          self.pratos.listapratos()
        case "4":
          self.menu_clientes()
          return