salario = float(input('Qual o seu salário atual? '))
aum = float(input('De quantos % será o aumento? '))
aumento = salario + (salario * aum / 100)
print('O seu salário com o aumento será de {:.2f}R$'.format(aumento))