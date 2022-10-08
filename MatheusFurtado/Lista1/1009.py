# https://www.beecrowd.com.br/judge/pt/problems/view/1009

NOME = input("")
SALARIO = float(input())
VENDAS = float(input())

TOTAL = SALARIO + (VENDAS * 0.15)

print("TOTAL = R$ %.2f" %TOTAL)