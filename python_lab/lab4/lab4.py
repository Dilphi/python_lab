t = ' '
print("13. Напишите программу которая подсчитывает количество ячеек в таблице, содержащей 5 строк и 2 столбца. При этом:")
print("13.1) внешний цикл проходит все ячейки таблицы по столбцам")
count = 0
for i in range(1,6):
    for j in range(2,4):
        count = count + 1
print(count)

print("13.2) внешний цикл проходит все ячейки таблицы по строкам")
count = 0
for j in range(2,4):
    for i in range(1,6):
        count = count + 1
print(count)

print("14. С помощью цикла for")
print("14.1) выведите на экран числа от 25 до 50")
for i in range(25, 50):
    print(i)

print("14.2) выведите на экран только чётные числа от 25 до 50")
for f in range(25, 50):
    if f % 2 == 0:
        print(f)

print("14.3) выведите на экран только нечётные числа от 25 до 50 без 45")
for f in range(25, 50):
    if f % 2 != 0 and f != 45:
        print(f)

print("15. С помощью цикла while")
print("15.1) выведите на экран числа от 50 до 25:")
num = 50
while num >= 25:
    print(num)
    num -= 1

print("15.2) выведите на экран только нечётные числа от 25 до 50:") 
num = 25
while num <= 50:
    if num % 2 != 0:
        print(num)
    num += 1

print("15.3) выведите на экран все чётные числа от 25 до 50, кроме числа 46, без директивы continue:")
num = 25
while num <= 50:
    if num % 2 == 0 and num != 46:
        print(num)
    num += 1
