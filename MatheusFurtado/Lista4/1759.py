# https://www.beecrowd.com.br/judge/pt/custom-problems/view/1759

anoAtual = int(input())

valorInicial = 1015

anos = anoAtual - 2006

valorSomado = 1015

contadorPorcentagem = 0.015 

somaPorcentagem = 0.01

if anoAtual < 2006:
    print("O ano informado deverá ser > 2005!")

elif anoAtual == 2006:
    print("Salário atual: R$%.2f"%(valorInicial))
    
 

elif anoAtual > 2006:
    porcentagem = (0.015 + 0.01)
    anoAnterior = valorInicial

    for i in range(anos):
        calculo = anoAnterior + (anoAnterior * porcentagem)
        anoAnterior = calculo
        porcentagem = porcentagem + 0.01

        
    print("Salário atual: R$%.2f"%(calculo))