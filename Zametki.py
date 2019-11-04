# ---------------------------------------------Командная строка----------------

# cd c:\
# cd %userprofile%
# cd %userprofile%\Documents
# dir - просмотр содержимого в папке
# echo %cd% - где находимся
# mkdir Имя - создать папку

# подключение пространства имен
# import sys
# доступ к параметру
# a = sys.argv[1]

# ---------------------------------------------Git-----------------------------

# git clone https://server/user/repo.git - клонирование репозитория
# git init - создание репозитория
# git config --global user.name "Alex Nikonov"
# git config --global user.email "alexeynico@gmail.com"
# git status
# git add - добавить файлы
# git commit -m "Первая версия" - сохранить
# git add -A - сохранить изменения

# ---------------------------------------------Типы данных---------------------

# -------------------------Целые числа
# сложение
a = 2
b = 3
c = a+b  # 5
# вычитание
a = 2
b = 3
c = a-b  # -1
# умножение
a = 2
b = 3
c = a*b  # 6
# в степень
a = 2
b = 3
c = a**b  # 8
# деление
a = 2
b = 3
c = a/b  # 0.6666666666 - вещественное число

# -------------------------Вещественные числа
# сложение
a = 2.5
b = 3.1
c = a+b  # 5.6
# вычитание
a = 2.5
b = 0.5
c = a-b  # 2.0
# результат деления - вещественное число

# -------------------------Строки
a = "Привет"
b = 'Привет'
a == b  # True

a = 'Привет'
b = 'мир'
a+b  # Приветмир
a + ', ' + b + '!'  # Привет, мир!

# Длина строки
len(a)
# Верхний регистр
a.upper()
# Нижний регистр
a.lower()
# Предложение
a.capitalize()
# Все с заглавной
a.title()
# Удаление пробелов из начала и конца
a.strip()
# Замена в строке
a = a.replace("П", "п")
# Разбиение строки в список
a = "learn.python.ru".split('.')


# -------------------------Форматирование строк
a = 'Привет'
b = 'мир'
# format приводит любые аргументы к строке
# Вариант 1
c = '{}, {}!'.format(a, b)
# Вариант 2
c = '{one}, {two}!'.format(one=a, two=b)
# Вариант 3
c = f'{a}, {b}!'

# -------------------------Ввод данных от пользователя (всегда строка)---------

# name = input('Введите ваше имя:\n')
# print(f'Привет, {name}!')

# -------------------------Приведение типов
int('2')
float(2)
bool(0)
str(9)

# ---------------------------------------------Срезы---------------------------

karta = "4532151219948973"

karta[:4]
# первые четыре символа

karta[-4:]
# последние четыре символа

karta[12:16]
# последние четыре символа

karta[-4:len(karta)]
# последние четыре символа

# ---------------------------------------------Методы строк--------------------

# "новая строка" ('\n'), "перевод каретки" ('\r'),
# "горизонтальная табуляция" ('\t') и "вертикальная табуляция" ('\v'))
S = 'Строка'

S.find("р")
# Поиск подстроки в строке.Возвращает номер первого вхождения или -1

S.rfind("р")
# Поиск подстроки в строке. Возвращает номер последнего вхождения или -1

S.isdigit()
# Состоит ли строка из цифр

S.isalpha()
# Состоит ли строка из букв

S.isalnum()
# Состоит ли строка из цифр или букв

S.islower()
# Состоит ли строка из символов в нижнем регистре

S.isupper()
# Состоит ли строка из символов в верхнем регистре

S.isspace()
# Состоит ли строка из неотображаемых символов (пробел, символ перевода
# страницы ('\f'), "новая строка" ('\n'), "перевод каретки" ('\r'),
# "горизонтальная табуляция" ('\t') и "вертикальная табуляция" ('\v'))

S.istitle()
# Начинаются ли слова в строке с заглавной буквы

S.startswith("str")
# Начинается ли строка S с шаблона str

S.endswith("str")
# Заканчивается ли строка S шаблоном str

S.join('список')
# Сборка строки из списка с разделителем S

ord("A")
# Символ в его код ASCII

chr(12)
# Код ASCII в символ

S.lstrip()
# Удаление пробельных символов в начале строки

S.rstrip()
# Удаление пробельных символов в конце строки

S.partition("шаблон")
# Возвращает кортеж, содержащий часть перед первым шаблоном, сам шаблон, и
# часть после шаблона. Если шаблон не найден, возвращается кортеж, содержащий
# саму строку, а затем две пустых строки

S.rpartition("sep")
# Возвращает кортеж, содержащий часть
# перед последним шаблоном, сам шаблон, и часть после шаблона.
# Если шаблон не найден, возвращается кортеж, содержащий две
# пустых строки, а затем саму строку

S.swapcase()
# Переводит символы нижнего регистра в верхний, а верхнего – в нижний

S.zfill(100)
# Делает длину строки не меньшей width,
# по необходимости заполняя первые символы нулями

S.ljust(100, " ")
# Делает длину строки не меньшей width,
# по необходимости заполняя последние символы символом fillchar

S.rjust(100, " ")
# Делает длину строки не меньшей width,
# по необходимости заполняя первые символы символом fillchar

S.center(100, " ")
# Возвращает отцентрованную строку,
# по краям которой стоит символ fill (пробел по умолчанию)

S.count("str", 0, 100)
# Возвращает количество непересекающихся вхождений подстроки в диапазоне
# [начало, конец] (0 и длина строки по умолчанию)

# ---------------------------------------------Списки-------------------------

phones = ["iPhone Xs", "Samsung Galaxy S10", "Xiaomi Mi8"]
# Список

len(phones)
# количество элементов списка

phones.append("Nokia")
# добавление элемента

count = phones.count("Nokia")
# количество элементов в списке

phones[1]
# обращение по индексу

phones[1:3]
# срезы работают по элементам

phones.index("Nokia")
# получение индекса элемента

phones.sort()
# сортировка

"Nokia" in phones
# проверка наличия элемента в списке

del phones[0]
# удаление элемента по индексу

phones.remove("Samsung Galaxy S10")
# удаление по значению. Если такого нет - будет ошибка
# удаляет первое попавшееся значение

# ---------------------------------------------Словари--------------------------

product = {
    "name": "iPhone Xs",
    "stock": 5,
    "price": 65000.0
}

# Длина словаря
len(product)

# Добавление элемента
product["memory"] = 64

# Удаление элемента
del product["memory"]

# Изменение значения
product["name"] = 'iPhone Xs Plus'
product["stock"] = 20

# Получение данных по ключу
product["name"]

# Безопасное обращение к ключу. Если ключа нет, будет None
product.get("name")

# Безопасное обращение к ключу. Если ключа нет, будет 10
product.get("name", 10)

# Вложить список в словарь
product["recomend"] = phones
# Обратиться к ключу вложенного словаря
product["recomend"][1]
# Добавить элемент во вложенный список
product["recomend"].append("iPhone 6")

# Список словарей
stock = [
    {"name": "iPhone Xs Plus", "stock": 24, "price": 65432.1,
        "recomend": ["Samsung Galaxy S10", "iPhone Xs"]},
    {"name": "Samsung Galaxy S10", "stock": 8, "price": 50000.0,
        "discount": 5000},
    {"name": "Xiaomi Mi8", "stock": 42, "price": 38000.5},
]
# Обращение
# print(stock[1]["name"])

# ---------------------------------------------Функции--------------------------
# с позиционными аргументами


def discounted(price, discount):
    price = abs(float(price))
    discount = abs(float(discount))
    if discount >= 100:
        price_with_discount = price
    else:
        price_with_discount = price - (price*discount/100)
    return price_with_discount

# именованые аргументы (со значениями по умолчанию)


def discounted2(price, discount, max_discount=50):
    price = abs(float(price))
    discount = abs(float(discount))
    max_discount = abs(float(max_discount))
    if max_discount > 99:
        raise ValueError('Максимальная скидка не более 99%')
    if discount >= max_discount:
        price_with_discount = price
    else:
        price_with_discount = price - (price*discount/100)
    return price_with_discount
