# https://www.beecrowd.com.br/judge/pt/custom-problems/view/1733

nome = input("")
horasExtras = float(input())
valorHoraExtra = 10.00
salarioMinimo = 1192.40

salarioHoraExtra = horasExtras * valorHoraExtra
salarioBruto = 3 * salarioMinimo + salarioHoraExtra

if salarioBruto > 2000:
    descontoInss = salarioBruto * 0.12
else:
    descontoInss = salarioBruto * 0.05

if salarioBruto > 2500:
    descontoIr = salarioBruto * 0.20


descontos = descontoIr + descontoInss
salarioLiquido = salarioBruto - descontos

print("Nome: %s \n Salário bruto: R$%.2f \n Salário líquido: R$%.2f" %(nome, salarioBruto, salarioLiquido))