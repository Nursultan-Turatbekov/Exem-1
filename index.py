# Задание 1.
lst = [92, 91, 49, 87, 74, 20, 94, 12, 64, 36, 97, 2, 96, 40, 97, 36, 32, 22, 80, 83, 49, 52, 62, 31,
55, 86, 84, 1, 22, 15, 52, 18, 78, 92, 21, 9, 85, 89, 54, 99, 80, 7, 4, 31, 30, 28, 59, 35, 72, 33]

dic = {}
for i in range(len(lst)):
    dic['' + str(i + 0)] = lst[i]

print(dic)    


# Задание 2.
import random

n = random.randint(1, 20)
for i in range(5):
    g = int(input('Введите число от 1 до 20: '))
    if g == n:
        print("Класс вы угадали")
        break 
    elif g < n:
        print("Слишком мало")
    elif g > n:
        print("Слишком много") 
if g != n:
    print('Все, вы не выиграли. Игра завершилась.')  


# Задание 3.
  
some_string = 'Adverts'
print(some_string[2:5])


# Задание 4.
a = "Aidana"
b = "Adilet"

c = ''.join(map(''.join, zip(a, b)))
print(c)





