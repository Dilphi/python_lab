name = "Руслан"
age = "19"
print("Меня зовут", name, "и мне", age)

a = 6
b = 9
print(a+b, a-b, a*b, a/b)

name = input("Введите своё имя: ")
age = input("Сколько вам лет? ")
print("Здравствуйте", name, "вам", age, "лет?")

print("Проверка чисел на чётность и нечётность")
num = int(input("Введите число: "))
print("Чётное" if num % 2 == 0 else "Нечётное")

text = "Python - это что-то"
print(text.upper())
print(text.lower())
print(len(text))
print(text.replace("что-то","интересно"))