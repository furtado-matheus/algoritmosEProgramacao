# https://www.beecrowd.com.br/judge/pt/custom-problems/view/1761

somaCompras = 0
troco = 0
while True:
    n1 = float(input(''))
    if n1 == 0:
        n2 = float(input(''))
        troco = n2 - somaCompras
        break
    else:
        somaCompras = somaCompras + n1
print("Total da compra: R$%.2f"%(somaCompras))
print("Valor pago: R$%.2f"%(n2))
print("Troco: R$%.2f"%(troco))