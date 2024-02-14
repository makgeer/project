from ru_converter import *
from en_converter import *

'''# общий модуль логики'''

def precoint(var = 1):
	
		if convert1 == 1:
			type_temp = int(input("Введите тип температуры:\n 1.Forengate\n 2.Kelvin\n:"))
			temp = float(input("Введите значение температуы:\n"))
			return "Получаем: %.2f" % (temper(type_temp, temp))
		elif convert1 == 2:
			type_mass = int(input(" Введите тип массы:\n1. Граммы -> унции\n2. Килограммы -> фунты\n"
				"3. Килограммы -> стоун\n4. Килограмм -> квинтал\n5. Килограмм -> центал\n6. Килограмм -> короткая тонна'us'\n"
				"7. Килограмм -> длинная тонна 'br'"))
			mass = float(input("Введите значение массы: "))
			return "Получаем: %.2f" % (massa(type_mass, mass))
		elif convert1 == 3:
			type_length = int(input(
				"Введите тип длинны:\n1. Километры -> мили\n"
				"2. Метры -> Ярды\n3. Метры -> футы\n4. Метры -> дюймы"
				"5. Сантиметры -> дюймы\n"
				"6. Миллиметры -> дюймы \n"))
			length = float(input("Введите значение длинны: "))
			return "Получаем: %.2f" % (lengths(type_length, length))
		elif convert1 == 4:
			pass
			return
		elif convert1 == 5:
			type_speed = int(input(
				"Ввыберите единицы конвертации:\n1. Колометры в час -> Мили в час\n2. Километры в час -> Кабельтов в час\n"
				"3. Метр в секунду - Узел в секунду\n 4. Махи в час -> Километры в час"))
			speed = float(input("Введите значение:\n"))
			return "Получаем: %.2f" % (speed_con(type_speed, speed))
	
def precoint(var = 2):
			
		if convert == 1:
			type_temp = int(input("Введите тип температуры:\n 1.Forengate\n 2.Kelvin\n:"))
			temp = float(input("Введите значение температуы:\n"))
			return "Получаем: %.2f" % (temper_1(type_temp, temp))
		elif convert == 2:
			type_mass = int(input("Введите тип массы:\n1. Граммы <- унции\n2. Килограммы <- фунты\n"
				"3. Килограммы <- стоун\n4. Килограмм <- квинтал\n5. Килограмм <- центал\n6. Килограмм <- короткая тонна'us'\n"
				"7. Килограмм <- длинная тонна 'br'"))
			mass = float(input("Введите значение массы: "))
			return "Получаем: %.2f" % massa_1(type_mass, mass)
		elif convert == 3:
			type_length = int(input(
				"Введите тип длинны:\n1. Километры <- мили\n "
				"2. Метры <- Ярды\n 3. Метры <- футы\n4. Метры <- дюйм"
				"5. Сантиметры <- дюймы\n"
				"6. Миллиметры <- дюймы \n"))
			length = float(input("Введите значение длинны: "))
			return "Получаем: %.2f" % lengths_1(type_length, length)
		elif convert == 4:
			pass
			return
		elif convert == 5:
			type_speed = int(input(
				"Ввыберите единицы конвертации:\n1. Колометры в час <- Мили в час\n2. Километры в час <- Кабельтов в час\n"
				"3. Метр в секунду <- Узел в секунду\n 4. Махи в час <- Километры в час"))
			speed = float(input("Введите значение:\n"))
			return "Получаем: %.2f" % speed_con_1(type_speed, speed)


'# в дальнейшем преобразовать в f-STRING'
'# расчет конвертации'

	
	
while True:
	var = input("1: Ru - Eng\n2: Eng - Ru\n Для завершения программы - наберите exit или нажмите клавишу 'q'\n")
	
	if var == 'q' or var == 'Q' or var == 'exit' or var == 'Exit':
		print('Программа завершена, спасибо за использование.\nThe program is complete, thanks for using it.')
		break
	var = int(var)
	if var == 1:
			print("Конвертер 0.2")
			convert = int(input("Что считаем: \n 1. Температура\n 2. Вес\n "
                        "3. Длина\n 4. Объем\n 5. Скорость\n "))
			print(precoint())
	elif var == 2:
		print("Converter 0.2")
		convert = int(input("What would you like to count:\n1. Temperature\n2. Weight\n3. Lenght\n4."
						" Volume\n5. Speed\n"))
		print(precoint())
