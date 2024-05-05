limite_peso = 50
m = 4
peso_peixes = float(input('Digite o peso dos peixes em kg: '))
if peso_peixes > limite_peso:
    excesso = peso_peixes - limite_peso
    multa = excesso * m
    print('Multa a pagar: R${:.2f}'.format(multa))
else:
    print('Dentro do limite.')