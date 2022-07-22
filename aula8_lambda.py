contador_letras = lambda lista: [len(x) for x in lista]

lista_animais = ['cachorro', 'gato', 'galinha']
print(contador_letras(lista_animais))

soma = lambda a, b: a + b
print(soma(1, 2))

calculadora = {
    'soma': lambda a, b: a + b,
    'subtracao': lambda a, b: a - b,
    'multiplicacao': lambda a, b: a  * b,
    'divisao': lambda a, b: a / b,
}

print(type(calculadora))
soma = calculadora['soma']
# soma = lambda a, b: a + b
multiplicacao = calculadora['multiplicacao']
print('A soma é {}' .format(soma(2, 4)))
print('A multiplicadcao é {}' .format(multiplicacao(3, 5)))