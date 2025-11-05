from classe_out import Pessoa, Morada

m1 = Morada("Rua 1", 1100123, 4, "5F")

print(m1.rua)

pessoa = Pessoa("Gonçalo", 20, 1.70, m1)

print(pessoa.nome)
