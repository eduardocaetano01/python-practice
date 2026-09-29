larg = float(input('Quantos metros de largura tem essa parede? '))
alt = float(input('Quantos metros de altura tem essa parede? '))
area = larg * alt
print('Sua parede tem a dimensão de {}x{} e sua área é de {}m².'.format(larg, alt, area))
tinta = area / 2
print('Para pintar essa parede, você precisará de {}l de tinta.'.format(tinta))