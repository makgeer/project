# -*-coding:utf-8-*-
# пересчет температур
def temper(type_temp: int, temp: float) -> float:
    """
    Программа вычисляет температуру приведенную в градусах цельсия
    и возвращает ее в кельвинах или форенгейтах
    :type.temp1 (int): принимает параметр кельвин
    :type.temp2 (int): принимает параметр форенгейт
    :param temp: тип данных возвращаемый функцией (float)
    :return: это мне подсказали, почему -1.0 не смог разобраться))

    """
    if type_temp == 1:
        return temp * 1.8 + 32
    if type_temp == 2:
        return temp + 273.15
    return -1.0


# пересчет масс
def massa(type_mass: int, mass: float) -> float:
    """

    :param type_mass:
    :param mass:
    :return:
    """
    if type_mass == 1:
        return mass * 0.035273998
    if type_mass == 2:
        return mass * 2.2046
    if type_mass == 3:
        return mass * 0.157473
    if type_mass == 4:
        return mass / 50.6
    if type_mass == 5:
        return mass / 45.3
    if type_mass == 6:
        return mass / 907.18
    if type_mass == 7:
        return mass / 1016
    return -1.0


def lengths(type_length: int, length: float) -> float:
    if type_length == 1:
        return length * 1.60934
    if type_length == 2:
        return length * 1.09361
    if type_length == 3:
        return length / 0.30481
    if type_length == 4:
        return length * 2.5400013716
    if type_length == 5:
        return length / 0.0393701
    return -1.0


def precoint():
    if convert == 1:
        type_temp = int(input("Введите тип температуры:\n 1.Forengate\n 2.Kelvin\n:"))
        temp = float(input('Введите значение температуы:\n'))
        return ("Получаем: %.3f" % temper(type_temp, temp))
    if convert == 2:
        type_mass = int(input("Введите тип массы:  1. Килограммы -> фунты\n 2. Граммы -> унции \n "))
        mass = float(input("Введите значение массы: "))
        return ("Получаем: %.3f" % massa(type_mass, mass))
    if convert == 3:
        type_length = int(input(
            "Введите тип длинны: ' 1. Километры -> мили\n 2. Метры -> Ярды\n 3. Метры -> футы\n 4. Сантиметры ->"
            " дюймы\n 5. Миллиметры -> дюймы \n' "))
        length = float(input("Введите значение длинны: "))
        return ("Получаем: %.3f" % lengths(type_length, length))


# в дальнейшем преобразовать в f-STRING
# расчет конвертации
var = int(input('1: Ru - Eng\n2: Eng - Ru\n'))
if var == 1:
    print('Конвертация из метрической в неметрическую')
    convert = int(input('Что считаем: \n 1. Температура\n 2. Вес\n 3. Длина\n 4. Объем\n 5. Скорость\n '))
    print(precoint())
