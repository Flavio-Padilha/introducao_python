from aula7_calculadora1 import Calculadora
from aula8_contador_letras import contador_letras

if __name__ == '__main__':
    calculadora = Calculadora(2,1)
    print(calculadora.soma())
    lista = ['cachorro', 'gato', 'elefante', 'macaco']
    total_letras = contador_letras(lista)
    print('Total de letras por palavra da lista: {} '.format(total_letras))