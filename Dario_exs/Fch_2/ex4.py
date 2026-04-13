# Exercício 4: Desconto de Cheque 
saldo = float(input("Saldo inicial: "))
cheque = float(input("Valor do cheque: "))

if cheque <= saldo:
    saldo -= cheque
    print(f"Cheque descontado, o teu novo saldo é de: {saldo:.0f}")
else:
    print("O cheque não pode ser descontado (Não tem saldo o suficiente).")