def maior(list):
    maior = list[0] 
    for num in list[1:]: # Começa no primeiro indice porque o menor ja é igual ao indice 0
        if num > maior: # Se o numero for maior que o primeiro, a variavel maior vai se tornar nesse numero
            maior = num
    
    return maior

def menor(list):
    menor = list[0]
    for num in list[1:]: # Começa no primeiro indice porque o menor ja é igual ao indice 0
        if num < menor: # Se o numero for menor que o primeiro, a variavel menor vai se tornar nesse numero
            menor = num
            
    return menor

while True:
    try:
        amt= int(input("Insira a quantidade de numeros que vai inserir na lista: ")) # Recebe o valor da quantidade de numeros para a lista
        
        #Faz com que seja preciso que o numero seja maior que 0
        if amt <=0:
            print("Insira um valor inteiro maior que 0!!!")
            continue
        
        break 
    
    # Se o valor inserido nao for numerico vai dar este erro
    except ValueError:
        print("Insiriu um valor invalido!!!")

list1=[]


for i in range(amt): # Loop para inserir cada numero da lista
    while True:
        try:
            num= int(input(f"Insira o {i+1} inteiro para adicionar à sua lista: ")) # Recebe cada numero da lista, tambem mostrando em que numero se encontra ( {i+1} )
            
            #Faz com que seja preciso que o numero seja maior ou igual a 0
            if num < 0:
                print("O numero insirido precisa ser maior ou igual a 0") 
                continue
            else:
                list1.append(num)
                break   
        
        # Se o valor inserido nao for numerico vai dar este erro
        except ValueError:
            print("ERRO! Deves inserir um numero inteiro!!!!")
            
            
print("Resultado:")
print(f"Numeros da lista: {list1} " ) # mostra os numeros da lista
print(f"O maior numero: {maior(list1)}") # mostra o maior numero da lista
print(f"O menor numero: {menor(list1)}") # mostra o menor numero da lista