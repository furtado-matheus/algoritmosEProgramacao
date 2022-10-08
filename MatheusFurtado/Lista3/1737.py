# https://www.beecrowd.com.br/judge/pt/custom-problems/view/1737

quantidadeNumeros = int(input(""))
valorAcumulado = 0 

if quantidadeNumeros <=0:
    print("Informe uma quantidade >0!")

else:
    while quantidadeNumeros > 0:
        numero = float(input(""))
        valorAcumulado = valorAcumulado + numero 
        quantidadeNumeros = quantidadeNumeros - 1
    print("Soma dos números informados: %.2f" %(valorAcumulado))