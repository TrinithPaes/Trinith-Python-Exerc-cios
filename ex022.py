nome = str(input('Digite seu nome completo: ')).strip()
print('Analisando seu nome...')
print('Nome com letras maiúsculas {} '.format(nome.upper()))
print('Nome com letras minusculas {} '.format(nome.lower()))
print('O nome tem {} letras'.format(len(nome) - nome.count(' ')))
print('Seu primeiro nome tem {} letras'.format(nome.find(' ')))

