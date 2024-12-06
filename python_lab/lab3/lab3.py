print("№1. Получите следующий список:[0, 'a', 1, 'b', 2, 'c']")
tst = {
	'1': 'a',
	'2': 'b',
	'3': 'c',
	'4': 'd'
}
result = []
for i, (key, value) in enumerate(tst.items()):
    if i < 3:
        result.append(i)
        result.append(value)
print(result)

print("№2 Дана пустая строка. Заполните с помощью цикла четными числами от 1 до 20.")
for ind in range(1,21):
    if ind % 2 == 0:
        print(ind)

print("№3 Выведите с помощью цикла столбец нечетных чисел от 100 до 1.")
num = []
for ind in range(1, 100):
    if ind % 2 != 0:
        num.append(ind)
num.sort(reverse=True)
print(num)

print("№4 Заполните список 10-ю иксами с помощью цикла.")
list = []
for index in range(10):
    list.append("x")
print(list)

print("№5 Заполните множество с помощью цикла первыми 10-ю буквами английского алфавита.")
alphabet_set = []
for letter in "abcdefghij":
    alphabet_set.append(letter)
alphabet_set.sort()
print(alphabet_set)

print("Второй")
alphabet_set = set()
for letter in "abcdefghij":
    alphabet_set.add(letter)
print(alphabet_set)

print("№6 Дан кортеж с числами. С помощью цикла выведите только те элементы, которые меньше меньше 10 и больше 5.")
cartech = []
for index in range(1,11):
    if index < 10 and index > 5:
        cartech.append(index)
print(cartech)

print("№7 Дана строка. С помощью цикла проверьте, есть ли в ней буква 'c'.")
string = input()
for inde in string:
    if inde == 'с':
        print("Есть")
    else:
        print("Отсутствует")

print("№8 Дан список с числами. Найдите среднее арифметическое его элементов.")
num = [1, 2, 3, 4, 5]
if len(num) > 0:
    average = sum(num) / len(num)
    print("Среднее арифметическое:", average)

print("№9 Дан список с числами. Переберите все его элементы до тех пор, пока не обнаружится положительное число.")
list = [-1,-2,-5,-9,2,-5]
for index in list:
    if index > 0:
        print(index)
print("№10 Дан словарь с именем, фамилией и возрастом пяти пользователей. Выведите все элементы словаря в виде кортежа ключ-значение.")
users = {
    'Павел Дуров': '11.09.2001', 
    'Геральт из Рыбии': '1167 год',
    'Хиро Хито':' 29.04.1901',
    'Владислав Ровнов':'23.8.2006'
}

for key, value in users.items():
    print((key, value))
print("№11 Из словаря в предыдущей задачи выведите в столбик все имена пользователей. При этом пусть они все будут написаны с большой буквы")
users = {
    'Павел': '11.09.2001', 
    'Геральт ': '1167 год',
    'Хиро': '29.04.1901',
    'Владислав Ровнов': '23.8.2006'
}

for name in users.keys():
    print(name.upper())