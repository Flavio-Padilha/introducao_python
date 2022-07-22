a = int(input('Primeiro valor:'))
b = int(input('Segundovalor: '))
soma = a+b
subtracao = a - b
multiplicacao = a * b
divisao = a / b
resto = a % b
# print('soma: ' + str(soma))
# print('subtracao: ' + str(subtracao))
# print('multiplicacao: ' + str(multiplicacao))
# print('divisao:' + str(divisao))
# print('resto: ' + str(resto))

resultado = ('Soma: {som}. '
      '\nDivisao: {div}. '
      '\nSubtracao: {sub}. '
      '\nMultiplicacao: {mult}. '
      '\nResto: {resto}.' .format(som=soma,
                                  sub=subtracao,
                                  mult=multiplicacao,
                                  div=divisao,
                                  resto=resto))

print(resultado)