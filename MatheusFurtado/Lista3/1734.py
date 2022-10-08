# https://www.beecrowd.com.br/judge/pt/custom-problems/view/1734

numero = int(input("") )

x = numero

resultado=1
count=1

while count <= numero:
    resultado *= count
    count += 1

print("%i! = %i" %(x, resultado))