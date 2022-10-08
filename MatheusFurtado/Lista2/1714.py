# https://www.beecrowd.com.br/judge/pt/custom-problems/view/1714

valorProduto = float(input())

porcentagemLucroMenor = valorProduto * 0.30
porcentagemLucroMaior = valorProduto * 0.45

totalLucroMenor = valorProduto + porcentagemLucroMenor
totalLucroMaior = valorProduto + porcentagemLucroMaior

if valorProduto < 20.00: 
    print ("Valor de venda: R$%.2f" %totalLucroMaior)
else:
    print("Valor de venda: R$%.2f" %totalLucroMenor)