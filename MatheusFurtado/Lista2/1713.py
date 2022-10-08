# https://www.beecrowd.com.br/judge/pt/custom-problems/view/1713

valorHora= float(input())
horasTrabalhadas = float(input())

salarioBruto = valorHora * horasTrabalhadas
IR = salarioBruto * 0.11
INSS = salarioBruto * 0.08
Sindicato = salarioBruto * 0.05
Impostos = IR + INSS + Sindicato
SalarioLiquido = salarioBruto - Impostos

print("Salário bruto: R$%.2f \n Imposto: R$%.2f \n INSS: R$%.2f \n Sindicato: R$%.2f \n Líquido: R$%.2f" %(salarioBruto, IR, INSS, Sindicato, SalarioLiquido))