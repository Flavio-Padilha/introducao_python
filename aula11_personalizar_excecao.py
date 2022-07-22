class Error (Exception):
    pass

class InputError (Error):
    def __init__(self, message):
        self.message = message

while True:
    try:
        nota_1 = int(input('Digite a nota do primeiro bimestre(valor de 0 a 10): '))
        print(nota_1)
        if nota_1 > 10:
            raise InputError('Nota não pode ser maior que 10.')
        elif nota_1 < 0:
            raise InputError('Nota não pode ser menor que 0.')
        break
    except ValueError:
        print('Valor inválido. Deve-se digitar apenas números.')
    except InputError as ex:
        print(ex)