class Calculadora:
    def __init__(self):
        pass

    def soma(self, valor_a, valor_b):
        return valor_a + valor_b

    def subtracao(self, valor_a, valor_b):
        return valor_a - valor_b

    def multiplicacao(self, valor_a, valor_b):
        return valor_a * valor_b

    def divisao (self, valor_a, valor_b):
        return valor_a / valor_b

# print(soma(1, 2))
# print(soma(3, 9))
# print(subtracao(2, 5))
# print(multiplicacao(10, 2))
# print(divisao(10, 2))

calculadora = Calculadora()
print(calculadora.soma(11, 1))
print(calculadora.subtracao(2, 1))
print(calculadora.multiplicacao(2, 15))
print(calculadora.divisao(15, 3))