from ru_converter import *
from en_converter import *


def precount():
    if convert == 1:
        type_temp = int(input("Введите тип температуры:\n 1.Foreshorten\n 2.Kelvin\n:"))
        temp = float(input("Введите значение температуы:\n"))
        return "Получаем: %.2f" % (temper(type_temp, temp))
    elif convert == 2:
        type_mass = int(input(" Введите тип массы:\n1. Граммы -> унции\n2. Килограммы -> фунты\n"
                              "3. Килограммы -> стоун\n4. Килограмм -> квинтал\n"
                              "5. Килограмм -> центал\n6. Килограмм -> короткая тонна'us'\n"
                              "7. Килограмм -> длинная тонна 'br'"))
        mass = float(input("Введите значение массы: "))
        return "Получаем: %.2f" % (massa(type_mass, mass))
    elif convert == 3:
        type_length = int(input(
            "Введите тип длинны:\n1. Километры -> мили\n"
            "2. Метры -> Ярды\n3. Метры -> футы\n4. Метры -> дюймы"
            "5. Сантиметры -> дюймы\n"
            "6. Миллиметры -> дюймы \n"))
        length = float(input("Введите значение длинны: "))
        return "Получаем: %.2f" % (lengths(type_length, length))
    elif convert == 4:
        type_volume = int(input(
            "Введите тип объема:\n1. Миллилитр -> американская жидкая унция\n"
            "2. Миллилитр -> американская житкая чашка\n3. Миллилитр -> американская житкая пинта\n"
            "4. Литр -> американская житкая кварта\n5. Литр -> американский житкий галлон"
        ))
        volume_con = float(input("Введите значение объема:\n"))
        return "Получаем: %.2f" % volume(type_volume, volume_con)
    elif convert == 5:
        type_speed = int(input(
            "Выберите единицы конвертации:\n1. Колометры в час -> Мили в час\n2. Километры в час -> Кабельтов в час\n"
            "3. Метр в секунду - Узел в секунду\n4. Махи в час -> Километры в час\n"))
        speed = float(input("Введите значение:\n"))
        return "Получаем: %.2f" % (speed_con(type_speed, speed))


def precount_1():
    if convert == 1:
        type_temp = int(input("Введите тип температуры:\n 1.Foreshorten\n 2.Kelvin\n:"))
        temp = float(input("Введите значение температуы:\n"))
        return "Получаем: %.2f" % (temper_1(type_temp, temp))
    elif convert == 2:
        type_mass = int(input("Введите тип массы:\n1. Граммы <- унции\n2. Килограммы <- фунты\n"
                              "3. Килограммы <- стоун\n4. Килограмм <- квинтал\n"
                              "5. Килограмм <- центал\n6. Килограмм "
                              "<- короткая тонна 'us'\n"
                              "7. Килограмм <- длинная тонна 'br'\n"))
        mass = float(input("Введите значение массы: "))
        return "Получаем: %.2f" % massa_1(type_mass, mass)
    elif convert == 3:
        type_length = int(input(
            "Введите тип длинны:\n1. Километры <- мили\n "
            "2. Метры <- Ярды\n3. Метры <- футы\n4. Метры <- дюйм"
            "5. Сантиметры <- дюймы\n"
            "6. Миллиметры <- дюймы\n"))
        length = float(input("Введите значение длинны: "))
        return "Получаем: %.2f" % lengths_1(type_length, length)
    elif convert == 4:
        type_volume = int(input(
            "Введите тип объема:\n1. Миллилитр -> американская жидкая унция\n"
            "2. Миллилитр -> американская житкая чашка\n3. Миллилитр -> американская житкая пинта\n"
            "4. Литр -> американская житкая кварта\n5. Литр -> американский житкий галлон"
            ))
        volume_con = float(input("Введите значение объема:\n"))
        return "Получаем: %.2f" % volume_1(type_volume, volume_con)
    elif convert == 5:
        type_speed = int(input(
            "Ввыберите единицы конвертации:\n1. Колометры в час <- Мили в час\n"
            "2. Километры в час <- Кабельтов в час\n"
            "3. Метр в секунду <- Узел в секунду\n4. Махи в час <- Километры в час\n"))
        speed = float(input("Введите значение:\n"))
        return "Получаем: %.2f" % speed_con_1(type_speed, speed)


'# в дальнейшем преобразовать в f-STRING'
'# расчет конвертации'
choose = 0

while True:
    choose = input("1: Ru - Eng\n2: Eng - Ru\n Для завершения программы - "
                   "наберите exit или 'q'\n")

    if choose == 'q' or choose == 'Q' or choose == 'exit' or choose == 'Exit':
        print('Программа завершена, спасибо за использование.\n'
              'The program is complete, thanks for using it.')
        break
    choose = int(choose)
    if choose == 1:
        print("Конвертер 0.2")
        convert = int(input("Что считаем: \n 1. Температура\n 2. Вес\n "
                            "3. Длина\n 4. Объем\n 5. Скорость\n "))
        print(precount())
    elif choose == 2:
        print("Converter 0.2")
        convert = int(input("What would you like to convertation:\n1. Temperature\n"
                            "2. Weight\n3. Length\n4."
                            " Volume\n5. Speed\n"))
        print(precount_1())
