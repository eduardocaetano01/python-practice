n1 = int(input('Digite um valor: '))
n2 = int(input('Digite outro valor: '))
s = n1+n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
mod = n1 % n2
e = n1 ** n2
print('A soma é {}, multiplicação é {}, divisão é {:.3f}, e a exponenciação é {}'.format(s, m, d, e), end=', ')
print('O modulo é: {}, e a divisão inteira é: {}'.format(mod, di))