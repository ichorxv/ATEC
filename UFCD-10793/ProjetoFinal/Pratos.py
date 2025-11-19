
class Pratos():
    def __init__(self, pratos=None, bebidas=None, entradas=None, add_pratos=None, del_pratos=None):

        
        self.pratos = pratos
        self.add_pratos = add_pratos
        self.del_pratos = del_pratos
        self.bebidas = bebidas
        self.entradas = entradas
        
    def listapratos(self):
        self.entradas=["Cheese Rolls", "Asinhas de Frango", "Nachos", "Pão e Manteiga", "Azeitonas"]
        self.bebidas=["Sangria", "Iced tea", "Refrigerante", "Vinho", "Agua Ardente", "Água (da sanita)"]
        self.pratos=["Picanha", "Pizza", "Hamburger (Estilo Americano)", "Tomahawk", "Wagyu Beef", "Maminha"]
        print("\n--- ENTRADAS ---")
        for e in self.entradas:
            print("-", e)

        print("\n--- BEBIDAS ---")
        for b in self.bebidas:
            print("-", b)

        print("\n--- PRATOS PRINCIPAIS ---")
        for p in self.pratos:
            print("-", p)
        print()