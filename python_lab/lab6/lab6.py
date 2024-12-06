st1 = {'x','1','y','2','z'}
st2 ={1,2,3,4,5,6}
if len(st1) > len(st2):
    print(st1)
else:
    print(st2) 

num1 = 12345
num2 = 12321

# Преобразуем числа в множества цифр
digits1 = set(str(num1))
digits2 = set(str(num2))

# Проверяем, что все цифры из num2 есть в num1
res = digits2.issubset(digits1)
print(res)  # Выведет True, если все цифры num2 есть в num1, иначе False
