import os

# Открываем файл data.txt для чтения
file1 = open("data.txt", "r")

with open("adults.txt", "w") as adults_file:
    while True:
        # Считываем строку
        line = file1.readline()
        # Прерываем цикл, если строка пустая (конец файла)
        if not line:
            break
        # Преобразуем строку в число и проверяем, равна ли она 18
        if line.strip().isdigit() and int(line.strip()) == 18:
            adults_file.write(18)
       
        print(line.strip())

file1.close()
