# https://www.beecrowd.com.br/judge/pt/custom-problems/view/1760

contador = 4

qtdObesos = 0

idade = 0

while contador > 0:
    idadeDoNoia = int(input(""))
    pesoDoNoia = float(input(""))

    if pesoDoNoia > 90:
        qtdObesos = qtdObesos + 1
        idade = idade + idadeDoNoia
        contador = contador - 1 

    else:
        idade = idade + idadeDoNoia
        contador = contador - 1

media = idade / 4
print("Qtd pessoas > 90 Kg: %i" %(qtdObesos))
print("Idade média: %.2f" %(media))
