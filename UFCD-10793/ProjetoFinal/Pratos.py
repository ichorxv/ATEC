class Pratos():
    def __innit__(self, pratos, nome, bebidas, entradas,  add_pratos, del_pratos):
        
        self.pratos = pratos
        self.add_pratos = add_pratos
        self.del_pratos = del_pratos
        self.nome = nome
        self.bebidas = bebidas
        self.entradas = entradas
    
        entradas=["Cheese Rolls", "Asinhas de Frango", "Nachos", "Pão e Manteiga", "Azeitos"]
        bebidas=["Sangria", "Iced tea", "Refrigerante", "Vinho", "Agua Ardente", "Água (da sanita)"]
        pratos=["Picanha", "Pizza", "Hamburger (Estilo Americano)", "Tomahawk", "Wagyu Beef", "Maminha"]