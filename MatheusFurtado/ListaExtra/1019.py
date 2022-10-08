# https://www.beecrowd.com.br/judge/pt/problems/view/1019

segundos = int(input())

minutos = int(segundos/60)
segundos -= minutos*60
horas = int(minutos/60)
minutos -= horas*60

print(f'{horas}:{minutos}:{segundos}')