
a = int(input('Primeiro bimestre: '))
while a > 10:
    a = int(input('Valor incorreto. Digite notvamente: '))
b = int(input('Segundo bimestre: '))
while b > 10:
    b = int(input('Valor incorreto. Digite novamente: '))
c = int(input('Terceiro bimestre: '))
while c > 10:
    c = int(input('Valor incorreto. Digite novamente: '))
d = int(input('Quarto bimestre: '))
while d > 10:
    d = int(input('Valor incorreto. Digite novamente: '))
media = (a + b + c + d) / 4
print('Média: {}' .format(media))

# a = 0
# while a <= 10:
#     print(a)
#     a += 1

# for num in range (101):
#     div = 0
#     for x in range(1, num+1):
#         resto = num % x
#         # print(x, resto)
#         if resto == 0:
#             div += 1
#
#     if div == 2:
#         print(num)

# a = int(input('Escreva um número: '))
# div = 0
# for x in range(1, a+1):
#     resto = a % x
#     print(x, resto)
#     if resto == 0:
#         div += 1
#
# if div == 2:
#     print('Número {} é primo' .format(a))
# else:
#     print('Número {} não é primo' .format(a))

# for x in range(0, 10):
#     print(x)
