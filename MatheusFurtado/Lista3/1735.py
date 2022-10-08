# https://www.beecrowd.com.br/judge/pt/custom-problems/view/1735

valorInicial = int(input())
valorFinal = int(input())
x = valorInicial

while x >= valorFinal:
    print(x)
    x = x - 1
print("Fogo!")  