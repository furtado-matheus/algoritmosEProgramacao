# https://www.beecrowd.com.br/judge/pt/custom-problems/view/1715

tipoCliente = int(input())
valorTotalCompra = float(input())

tipoCliente2 = valorTotalCompra * 0.13
tipoCliente3 = valorTotalCompra * 0.07

totalTipo2 = valorTotalCompra - tipoCliente2
totalTipo3 = valorTotalCompra - tipoCliente3

if tipoCliente == 2:
    print("Valor total a ser pago: R$%.2f" %totalTipo2)
elif tipoCliente == 3:
    print("Valor total a ser pago: R$%.2f" %totalTipo3)
elif tipoCliente == 1:
    print("Valor total a ser pago: R$%.2f" %valorTotalCompra)
else:
    print("OPÇÃO INVÁLIDA!")