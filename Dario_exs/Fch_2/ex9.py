# Exercício Switch: Nome do Mês 

mes = int(input("Introduza um número de 1 a 12: "))

meses = {
    1: "Janeiro", 2: "Fevereiro", 3: "Março", 4: "Abril",
    5: "Maio", 6: "Junho", 7: "Julho", 8: "Agosto",
    9: "Setembro", 10: "Outubro", 11: "Novembro", 12: "Dezembro"
}

print(meses.get(mes, "ERRO!!! \nNumero invalido! O numero deve ser entre 1 e 12!"))