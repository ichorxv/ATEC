num=0
cont=0
cont2=0

num= int (input("insira um numero que queira adicionar ao contador: "))

while num >= 0:
    cont2+=1
    cont = cont+num
    num= int (input("insira um numero que queira adicionar ao contador: "))
    
media=cont/cont2
print(f"a quantidade total é de:", (cont) )
print(f"a media é de: ", (media))