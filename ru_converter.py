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
        return (temp * 1.8) + 32
    elif type_temp == 2:
        return temp - 273.15
    return -1.0


def massa(type_mass: int, mass: float) -> float:
    """пересчет масс"""

    """
    Программа принимает на вход вес в метрической системе
    на вывод преобразует в английскую.
    :param type_mass: метрическая
    :param mass: английская
    :return: возвращает преобразование
	"""

    if type_mass == 1:
        return mass * 0.035273998  # Граммы -> унции
    elif type_mass == 2:
        return mass * 2.2046  # Килограммы -> фунты
    elif type_mass == 3:
        return mass * 0.157473  # Килограммы -> стоун
    elif type_mass == 4:
        return mass / 50.802  # Килограмм -> квинтал
    elif type_mass == 5:
        return mass / 45.36  # Килограмм -> центал
    elif type_mass == 6:
        return mass / 907.18  # Килограмм -> короткая тонна
    elif type_mass == 7:
        return mass / 1016  # Килограмм -> длинная тонна
    return -1.0


def lengths(type_length: int, length: float) -> float:
    """ пересчет длины"""
    """
    Программа принимает на вход длину в метрической системе
    на вывод преобразует в английскую.
    :param type_length: метрическая система
    :param length: английская
    :return: возвращает преобразование
	"""

    if type_length == 1:
        return length / 1.60934  # Километры <- мили
    if type_length == 2:
        return length * 1.09361  # Метры <- ярды
    if type_length == 3:
        return length * 3.281  # Метры <- фунты
    if type_length == 4:
        return length * 39.37  # Метры <- дюйм
    if type_length == 5:
        return length / 2.5400013716  # Сантиметры <- дюйм
    if type_length == 6:
        return length / 25.4  # Миллиметры <- дюйм
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
        return speed / 1.60934  # километры в мили
    if type_speed == 2:
        return speed * 5.399  # километры в кабельтов
    if type_speed == 3:
        return speed / 0.30481  # метры в узлы
    if type_speed == 4:
        return speed * 900  # махи в километры
    return -1.0
def volume(type_volume: int, volume_con: float) -> float:
    if type_volume == 1:
        return volume_con * 1
    if type_volume == 2:
        return volume_con * 2
    if type_volume == 3:
        return volume_con * 3
    if type_volume == 4:
        return volume_con * 4
    if type_volume == 5:
        return volume_con *5
    return -1.0