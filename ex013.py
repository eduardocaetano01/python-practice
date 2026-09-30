salario = float(input('Qual o seu salário atual? R$'))
aum = float(input('De quantos % será o aumento?'))
aumento = salario + (salario * aum / 100)
print('Um funcionário que ganhava R${}, com {}% de aumento, passa a receber R${:.2f}'.format(salario, aum, aumento))
