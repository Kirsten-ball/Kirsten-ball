#Импортируем модули
from colorama import Fore, Style
import os
import time

#Калькулятор на питоне без обрабатывание ошибок
start_time = time.time()
os.system("clear")
print("Калькулятор")
#Первое число
calc1 = float(input(Fore.GREEN + "Введите число: "))
#Второе число
calc2 = float(input(Fore.GREEN + "Введите второе число: "))
#Знак операции
znak1 = input(Fore.YELLOW + "Введите знак операции: ")
#Переменные делающие операцию
plus = calc1 + calc2
minus = calc1 - calc2
ymni = calc1 * calc2
stepen = calc1 ** calc2
deyla = calc1 // calc2
dd = calc1 / calc2
#Прописываем код на исполнениеис использованием конструкции (if-elif-else)
if znak1 == "+":
	os.system("clear")
	print(plus)
elif znak1 == "-":
	os.system("clear")
	print(minus)
elif znak1 == "*":
	os.system("clear")
	print(ymni)
elif znak1 == "/":
	os.system("clear")
	print(dd)
elif znak1 == "**":
	os.system("clear")
	print(stepen)
elif znak1 == "//":
	os.system("clear")
	print(deyla)
#Если написано другое
#Можно было бы обработать ошибку
else:
	os.system("clear")
	print("Ошибка!")
end_time = time.time()
total_time = end_time - start_time
#Не знаю зачем тотальное время, но пусть будет
print(f"Полное время исполнения: {total_time}")