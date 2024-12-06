# Рекурсивный факториал
def factor(num):
    factor(num* num)

print(factor(5))

# Числа Фибоначчи
def fibon(n):
    if n == 1:
        return [0]
    elif n == 2:
        return [0, 1]

    sequence = [0, 1]  # Начинаем с первых двух чисел Фибоначчи
    for i in range(2, n):
        sequence.append(sequence[i-1] + sequence[i-2])
    return sequence

print(fibon(6))

#Лямбда-функции и сортировка
def sort_by_length(words):
    return sorted(words, key=lambda x: len(x))


print(sort_by_length(["apple", "banana", "kiwi", "pear"])) 
  

# Работа с аргументами переменной длины
def concat_strings(*args):
    return ''.join(args)

print(concat_strings("Hello", " ", "world!"))  # Hello world!
