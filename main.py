# -*-coding:utf-8-*-
# задание 1 + 3

a = input('Ведите цифру от 1 до 9:\n')
b = a + a
c = a + a + a
print(int(a) + int(b) + int(c))


# задание 2

a = int(input("Введите число секунд:\n "))
hour = a // 3600
minute = a // 60
if minute > 60:
    minute = minute // 60
    hour += 1
second = a % 60
print(f"{hour}:{minute}:{second}")

# задание 4

a = int(input("Введиет любое положительное число:\n"))
s = str(a)
ls = list(map(int, s))
r = max(ls)
print(r)
