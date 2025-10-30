
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

triplo = [3 * x for x in numeros]

print("Original:", numeros)
print("Triplo:  ", triplo)

#----------------------------------------

numeros = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]

inteiros=[]

inteiros = [(int(i)) for i in numeros]

print(inteiros)

#----------------------------------------

lista_mista = ["10", "abc", "25", "42", "hello", "7", "world", "99", "33", "foo", "bar", "123", "0", "9x", "88"]
lista_numerica = [int(x) for x in lista_mista if x.isdigit()]

print(lista_mista)
print(lista_numerica)

