"""пересчет температур"""


def temper(type_temp: int, temp: float) -> float:
    """
    Программа вычисляет температуру приведенную в градусах цельсия
    и возвращает ее в кельвинах или форенгейтах
    :param type_temp: принимает на вход задаваемый пользователем параметр
    :type type_temp : == 1 принимает параметр кельвин
    :type type_temp : == 2 принимает параметр форенгейт
    :param temp: тип данных возвращаемый функцией (float)
    :return: возвращает преобразование

    """
    if type_temp == 1:
        return temp * 1.8 + 32
    elif type_temp == 2:
        return temp + 273.15
    return -1.0


'# пересчет масс'


def massa(type_mass: int, mass: float) -> float:
    """
    Программа принимает на вход вес в метрической системе
    на вывод преобразует в английскую.
    :param type_mass: метрическая
    :param mass: английская
    :return: возвращает преобразование
    """
    if type_mass == 1:
        return mass * 0.035273998
    elif type_mass == 2:
        return mass * 2.2046
    elif type_mass == 3:
        return mass * 0.157473
    elif type_mass == 4:
        return mass / 50.6
    elif type_mass == 5:
        return mass / 45.3
    elif type_mass == 6:
        return mass / 907.18
    elif type_mass == 7:
        return mass / 1016
    return -1.0


'# пересчет длины'


def lengths(type_length: int, length: float) -> float:
    """
    Программа принимает на вход длину в метрической системе
    на вывод преобразует в английскую.
    :param type_length: метрическая система
    :param length: английская
    :return: возвращает преобразование
    """
    if type_length == 1:
        return length / 1.60934
    if type_length == 2:
        return length / 1.09361
    if type_length == 3:
        return length / 0.30481
    if type_length == 4:
        return length * 2.5400013716
    if type_length == 5:
        return length / 0.0393701
    return -1.0


def speed_con(type_speed: int, speed: float) -> float:
    """
    Программа принимает на вход длину в метрической системе
    на вывод преобразует в английскую.
    :param type_speed: метрическая система
    :param speed: английская
    :return: возвращает преобразование
    """
    if type_speed == 1:
        return speed / 1.60934  # киломтры в мили
    if type_speed == 2:
        return speed * 185.2  # километры в кабельтов
    if type_speed == 3:
        return speed / 0.30481  # метры в узлы
    if type_speed == 4:
        return speed * 900  # махи в километры
        return -1.0


'# общий модуль логики'


def precoint():
    if convert == 1:
        type_temp = int(input("Введите тип температуры:\n 1.Forengate\n 2.Kelvin\n:"))
        temp = float(input("Введите значение температуы:\n"))
        return "Получаем: %.3f" % temper(type_temp, temp)
    elif convert == 2:
        type_mass = int(input("Введите тип массы:\n  1. Килограммы -> фунты\n 2. Граммы -> унции \n "))
        mass = float(input("Введите значение массы: "))
        return "Получаем: %.3f" % massa(type_mass, mass)
    elif convert == 3:
        type_length = int(input(
            "Введите тип длинны:\n1. Километры -> мили\n "
            "2. Метры -> Ярды\n 3. Метры -> футы\n 4. Сантиметры -> дюймы\n"
            " 5. Миллиметры -> дюймы \n"))
        length = float(input("Введите значение длинны: "))
        return "Получаем: %.3f" % lengths(type_length, length)
    elif convert == 4:
        pass
        return
    elif convert == 5:
        type_speed = int(input(
            "Ввыберите единицы конвертации:\n1. Колометры в час -> Мили в час\n2. Километры в час -> Кабельтов в час\n"
            "3. Метр в секунду - Узел в секунду\n 4. Махи в час -> Километры в час"))
        speed = float(input("Введите значение:\n"))
        return "Получаем: %.3f" % speed_con(type_speed, speed)


'# в дальнейшем преобразовать в f-STRING'
'# расчет конвертации'
var = int(input("1: Ru - Eng\n2: Eng - Ru\n"))
if var == 1:
    print("Конвертер 0.2")
    convert = int(input("Что считаем: \n 1. Температура\n 2. Вес\n "
                        "3. Длина\n 4. Объем\n 5. Скорость\n "))

    print(precoint())
