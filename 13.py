while True:
    altura = float(input('Digite a altura em metros: '))
    sexo = input('Digite o sexo, M para masculino, F para feminino: ')
    if sexo.upper() == 'M':
        ps = (72.7 * altura) - 58
        print('Seu peso ideal é de {:.2f} kg.'.format(ps))
        break
    elif sexo.upper() == 'F':
        ps = (62.1 * altura) - 44.7
        print('Seu peso ideal é de {:.2f} kg.'.format(ps))
        break
    else:
        print('Por favor, digite uma opção válida. ')
