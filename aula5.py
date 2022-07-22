lista = [1, 3, 5, 7, 2, 33, 4]
lista_animal = ['cachorro', 'gato', 'elefante']
# print(lista[2])
# for x in lista_animal:
#     print(x)

animal = input('Digite um animal: ')
if animal in lista_animal:
     print('Existe o animal {}'.format(animal) + ' na lista!')
else:
    print('Não existe o animal {}'.format(animal) + ' na lista. Será incluído!')
    lista_animal .append(animal)
print(lista_animal)

lista.sort()
print(lista)

lista_animal.reverse()
print(lista_animal)