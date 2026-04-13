# Exercício 1: Converter Segundos 

segundos = int(input("Insira os segundos: "))

hrs = segundos // 3600
mins = (segundos % 3600) // 60
seg = segundos % 60

print(f"{hrs} hora(s), {mins} minuto(s) e {seg} segundo(s)\n")