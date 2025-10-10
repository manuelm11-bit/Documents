segundos = int(input("Digite o tempo em segundos: "))

horas = segundos // 3600
resto = segundos % 3600
minutos = resto // 60
segundo = resto % 60

print(f"segundoss equivalem a {horas}h {minutos}m {segundos}s")
