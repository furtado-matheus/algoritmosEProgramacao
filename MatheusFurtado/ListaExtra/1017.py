# https://www.beecrowd.com.br/judge/pt/problems/view/1017

tempo = int(input())
velocidadeMedia = int(input())

consumo = 12

op1 = velocidadeMedia/consumo
op2 = tempo * op1

print("%.3f"%(op2))