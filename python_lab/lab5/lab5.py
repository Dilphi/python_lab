dct = {'y': 2025, 'm': 12, 'd':31}
print(f'{dct["y"]}-{dct["m"]}-{dct["d"]}')

dct = { 'a': 7, 'b': 6, 'c': 5 }
print(f'{dct["c"]}/{dct["b"]}/{dct["a"]}')


tup = (1, 2, 3, 4, 5, 6)
even_numbers = []
odd_numbers = []

for i in tup:
    if i % 2 == 0:
        even_numbers.append(i)
    else:
        odd_numbers.append(i)

# Преобразуем списки в кортежи
even_tuple = tuple(even_numbers)
odd_tuple = tuple(odd_numbers)

print("Четные числа:", even_tuple)
print("Нечетные числа:", odd_tuple)


tup1 = (1, 2, 3, 4)
tup2 = (3, 4, 5, 6)

# Находим общие элементы, преобразуя кортежи во множества
common_elements = tuple(set(tup1) & set(tup2))

print("Общие элементы:", common_elements)


d = {'a': 1, 'b': 2, 'c': 3}
inverted_dict = {}

for key, value in d.items():
    inverted_dict[value] = key

print("Инвертированный словарь:", inverted_dict)
