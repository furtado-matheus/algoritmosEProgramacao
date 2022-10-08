# https://www.beecrowd.com.br/judge/pt/custom-problems/view/1716

tipoPlano = input("")
salarioAtual = float(input())

planoA = salarioAtual * 0.10
planoB = salarioAtual * 0.15
planoC = salarioAtual * 0.20

aumentoPlanoA = salarioAtual + planoA
aumentoPlanoB = salarioAtual + planoB
aumentoPlanoC = salarioAtual + planoC

if tipoPlano == "A":
    print("Novo salário: R$%.2f" %aumentoPlanoA)
elif tipoPlano == "B":
    print("Novo salário: R$%.2f" %aumentoPlanoB)
if tipoPlano == "C":
    print("Novo salário: R$%.2f" %aumentoPlanoC)
