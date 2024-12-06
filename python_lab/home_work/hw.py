# Напишите программу, которая найдет все такие числа, которые делятся на 7, но не кратны 5, в диапазоне от 2000 до 3200 (включая оба).
begin = 2000
end = 3000

# Список для хранения подходящих чисел
result = []

for i in range(begin, end + 1):
    if i % 7 == 0 and i % 5 != 0:
        result.append(str(i))
    print(",".join(result))


# Задача 2: Анализ финансовых транзакций
transactions = [200, -150, 300, -50, -250, 500, -100]

total_in = 0  # Общий доход
total_ex = 0 # Общий расход
in_count = 0  # Количество доходных транзакций
ex_count = 0 # Количество расходных транзакций
max_ex = float('-inf')  # Для поиска максимальной траты
max_ex_day = -1         # День с самой высокой тратой

# Перебор всех транзакций
for day, transaction in enumerate(transactions):
    if transaction > 0:
        total_in += transaction
        in_count += 1
    else:
        total_ex += transaction
        ex_count += 1
        # Определение самой высокой траты
        if transaction < max_ex:
            max_ex = transaction
            max_ex_day = day + 1  # Номер дня

# Вычисление средних значений дохода и расхода
average_in = total_in / in_count if in_count > 0 else 0
average_ex = total_ex / ex_count if ex_count > 0 else 0


print("Общая сумма доходов:", total_in)
print("Общая сумма расходов:", total_ex)
print("Средняя сумма дохода:", average_in)
print("Средняя сумма расхода:", average_ex)
print("День с самой высокой тратой:", max_ex_day)

# Напишите программу, вычисляющую факториал заданного числа.
import math;n = int(input("Введите число: "));factorial = math.factorial(n);print(factorial)