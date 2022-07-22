conjunto = {1, 2, 3, 4, 5}
conjunto2 = {5, 6, 7, 8, 9}
conjunto_uniao = conjunto .union(conjunto2)
print('União: {}' .format(conjunto_uniao))
conjunto_intersec = conjunto .intersection(conjunto2)
print('Intersecção: {}' .format(conjunto_intersec))
conjunto_dif1 = conjunto .difference(conjunto2)
print('Diferença entre 1 e 2: {}' .format(conjunto_dif1))
conjunto_dif2 = conjunto2 .difference(conjunto)
print('Diferença entre 2 e 1: {}' .format(conjunto_dif2))
conjunto_dif_sym = conjunto .symmetric_difference(conjunto2)
print('Diferença simétrica 1 e 2: {}' .format(conjunto_dif_sym))

conjunto_a = {1, 2, 3}
conjunto_b = {1, 2, 3, 4, 5}
conjunto_subset = conjunto_a .issubset(conjunto_b)
print('A é subset de b:{}' .format(conjunto_subset))
conjunto_superset = conjunto_b .issuperset(conjunto_a)
print('B é superset de a: {}' .format(conjunto_superset))

lista = ['cachorro', 'cachorro', 'gato', 'elefante', 'gato', 'girafa', 'macaco']
conjunto_animais = set(lista)
print(conjunto_animais)

# conjunto = {1, 2, 3, 4}
# conjunto .add(5)
# conjunto .discard(2)
# print(conjunto)
