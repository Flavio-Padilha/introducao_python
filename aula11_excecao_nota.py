class Error (Exception):
    pass

class InputError (Error):
    def __init__(self, message):
        self.message = message

while True:
    try:
        nota_1 = int(input('Digite a nota do primeiro bimestre(valor de 0 a 10): '))
        print('Primeiro bimestre: {}' .format(nota_1))
        if nota_1 > 10:
            raise InputError('Nota não pode ser maior que 10.')
        elif nota_1 < 0:
            raise InputError('Nota não pode ser menor que 0.')
        break
while True:
    and try:
        nota_2 = int(input('Digite a nota do segundo bimestre(valor de 0 a 10): '))
        print('Segundo bimestre: {}'.format(nota_2))
        if nota_2 > 10:
            raise InputError('Nota não pode ser maior que 10.')
        elif nota_2 < 0:
            raise InputError('Nota não pode ser menor que 0.')
        break
while True:
    try:
        nota_3 = int(input('Digite a nota do terceiro bimestre(valor de 0 a 10): '))
        print('Terceiro bimestre: {}'.format(nota_3))
        if nota_3 > 10:
            raise InputError('Nota não pode ser maior que 10.')
        elif nota_3 < 0:
            raise InputError('Nota não pode ser menor que 0.')
        break
while True:
    try:
        nota_4 = int(input('Digite a nota do quarto bimestre(valor de 0 a 10): '))
        print('Quarto bimestre: {}'.format(nota_4))
        if nota_4 > 10:
            raise InputError('Nota não pode ser maior que 10.')
        elif nota_4 < 0:
            raise InputError('Nota não pode ser menor que 0.')
        break
    except ValueError:
        print('Valor inválido. Deve-se digitar apenas números.')
    except InputError as ex:
        print(ex)