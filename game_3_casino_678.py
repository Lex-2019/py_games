# КАЗИНО 678

import time
import random
from ctypes import *  # стандартная библиотека цветов в пайтоне

currency = "руб."     # номинал валюты
money = 0             # количество денег в процессе игры
startMoney = 0        # количество денег на начало некой игры
playGame = True       # логическая переменная для определения, продолжать ли игру или закончить
defaultMoney = 10000  # начальные деньги, есть мысль начать с ввода с клавиатуры

# алгоритм изменения цвета в консоли Windows 10 x64:
windll.Kernel32.GetStdHandle.restype = c_ulong
h = windll.Kernel32.GetStdHandle(c_ulong(0xfffffff5))


# установка цвета текста
def color(c):
    windll.Kernel32.SetConsoleTextAttribute(h, c)


# вывод на экран цветного текста с обрамлением
def color_line(c, s):
    """
    for i in range(30):  # очистка экрана консоли от предыдущих результатов вывода
        print()
    """
    # альтернатива очистки экрана:
    import os
    os.system("cls")

    color(c)
    print("*" * (len(s) + 2))
    print(" " + s)
    print("*" * (len(s) + 2))
# a = color_line(15, "Привет! Я такой типа привлекаю внимание")
# print(a)


# вывод сообщения о выигрыше
def victory(result):
    color(14)
    print(f"    Победа за тобой! Выигрыш составил: {result} {currency}")
    print(f"    У тебя на счету: {money}")


# вывод сообщения о проигрыше
def losing(result):
    color(12)
    print(f"    К сожалению, проигрыш: {result} {currency}")
    print(f"    У тебя на счету: {money}")
    print("    Обязательно нужно отыграться!")


# функция ввода значения
def get_input(digit, message):
    color(7)
    ret = ""
    while ret == "" or ret not in digit:
        # выполнять, пока Символ ПУСТОЙ или символа НЕТ в СТРОКЕ digit
        ret = input(message)
    return ret
# print(f"Вы ввели число {get_input('0123', 'Введите от 1 до 3 или 0 для выхода! ')}")


# функция ввода целого числа (ставка)
def get_int_input(minimum, maximum, message):
    color(7)
    ret = -1  # заведомо неправильное значение
    while ret < minimum or ret > maximum:
        # пока пользователь ввел число меньше минимального значения или выше максимального
        st = input(message)
        if st.isdigit():
            ret = int(st)
        else:
            print("    Введи целое число!")  # пробелы в начале для красоты
    return ret
# a = get_int_input(0, 10, "Введи от 0 до 10: ")
# print(a)


# Чтение из файла оставшейся суммы
def load_money():
    try:
        f = open("money.dat", "r")
        m = int(f.readline())
        f.close()
    except FileNotFoundError:
        print(f"Файла не существует, задано значение {defaultMoney} {currency}")
        m = defaultMoney
    return m


# запись суммы в файл
def save_money(money_to_save):
    try:
        f = open("money.dat", "w")
        f.write(str(money_to_save))
        f.close()
    except:  # блок будет выполняться при любой ошибке!
        print("Ошибка создания файла, наше казино закрывается!")
        quit(0)


# Анимация рулетки и возвращение числа:
def get_roulette(visible):
    # Задаём переменные:
    # время в секундах, на которое увеличивается время паузы за одну итерацию цикла:
    tickTime = random.randint(100, 200) / 10000
    mainTime = 0                    # пауза в секундах
    number = random.randint(0, 38)  # номер, выпавший на рулетке
    # время в секундах, на которое увеличивается переменная tickTime для создания эффекта неравномерности в паузах:
    increaseTickTime = random.randint(100, 110) / 100
    col = 1                         # цвет выводимого сообщения

    # Главный цикл функции
    # Выполняется, пока пауза не станет 0.7 секунды и больше
    while mainTime < 0.7:
        # Изменение цвета:
        col += 1
        if col > 15:
            col = 1

        # Увеличение времени паузы:
        mainTime += tickTime
        tickTime *= increaseTickTime

        # Увеличение номера и вывод на экран:
        color(col)
        number += 1
        if number > 38:
            number = 0
            print()

        # Обработка "скрытых" от пользователя чисел 37 и 38, символизирующие "00" и "000"
        print_number = number
        if number == 37:
            print_number = "00"
        elif number == 38:
            print_number = "000"

        # Бесподобно эффектный вывод ;)
        print("Число >",
              print_number,
              "*" * number,
              " " * (79 - number * 2),
              "*" * number)

        # Делаем паузу в зависимости от переданного аргумента visible
        if visible:
            time.sleep(mainTime)

    # Возвращаем выпавшее на рулетке число
    return number


# Рулетка
def roulette():
    global money      # количество средств на счету игрока
    playGame = True   # маркер главного цикла метода рулетки
    print_number = ""
    duzhina = ""
    text_duzhina = ""
    chislo = 0
    # Главный цикл рулетки:
    while playGame and money > 0:
        # Вывод меню  игры:
        color_line(3, "ДОБРО ПОЖАЛОВАТЬ НА ИГРУ В РУЛЕТКУ!")
        color(14)
        print(f"\n У тебя на счету {money} {currency}\n")
        color(11)
        print(" Ставлю на...")
        print("    1. Чётное (выигрыш 1:1)")
        print("    2. Нечётное (выигрыш 1:1)")
        print("    3. Дюжина (выигрыш 3:1)")
        print("    4. Число (выигрыш 36:1)")
        print("    0. Возврат в предыдущее меню")

        # Выбор пункта меню:
        x = get_input("01234", "    Твой выбор? ")

        # маркер: нужно ли играть в рулетку?:
        playRoulette = True

        if x == "3":
            color(2)
            print()
            print(" Выбери числа:...")
            print("    1. От 1 до 12")
            print("    2. От 13 до 24")
            print("    3. От 25 до 36")
            print("    0. Назад")

            # Выбор пункта меню "дюжина":
            duzhina = get_input("0123", "    Твой выбор? ")

            if duzhina == "1":
                text_duzhina = "от 1 до 12"
            elif duzhina == "2":
                text_duzhina = "от 13 до 24"
            elif duzhina == "3":
                text_duzhina = "от 25 до 36"
            elif duzhina =="0":
                playRoulette = False
        # Если делаем ставку на "число":
        elif x == "4":
            chislo = get_int_input(0, 36, "    На какое число ставишь? (0..36): ")

        # если ввели "0" в меню рулетки:
        color(7)
        if x == "0":
            return 0

        if playRoulette:
            rate = get_int_input(0, money, f"    Сколько поставишь? (не больше {money}): ")  # ставка игрока
            if rate == 0:
                return 0

            # Анимация рулетки и получение номера:
            number = get_roulette(True)
            # Выводим полученное число:
            print()
            color(11)

            # В зависимости от значения number формируем вывод:
            if number < 37:
                print(f"    Выпало число {number}! " + "*" * number)
            else:
                if number == "37":
                    print_number = "00"
                elif number == "38":
                    print_number = "000"
                print(f"    Выпало число {print_number}! ")

            # Проверяем ставки и результат:
            if x == "1":
                print("    Ты ставил на ЧЁТНОЕ!")
                if number < 37 and number % 2 == 0:
                    money += rate
                    victory(rate)
                else:
                    money -= rate
                    losing(rate)
            elif x == "2":
                print("    Ты ставил на НЕЧЁТНОЕ!")
                if number < 37 and number % 2 != 0:
                    money += rate
                    victory(rate)
                else:
                    money -= rate
                    losing(rate)
            elif x == "3":
                print(f"    Ставка сделана на диапазон чисел {text_duzhina}.")
                winDuzhina = ""
                if 0 < number < 13:
                    winDuzhina = "1"
                elif 12 < number < 25:
                    winDuzhina = "2"
                elif 24 < number < 37:
                    winDuzhina = "3"

                if duzhina == winDuzhina:
                    money += rate * 2
                    victory(rate * 3)
                else:
                    money -= rate
                    losing(rate)
            elif x == "4":
                print(f"    Ставка сделана на число {chislo}.")
                if number == chislo:
                    money += rate * 35
                    victory(rate * 36)
                else:
                    money -= rate
                    losing(rate)
            # Ждём нажатия Enter и продолжаем:
            print()
            input(" Нажми Enter для продолжения...")


# Анимация костей
def get_dice():
    count = random.randint(3, 8)  # сколько раз будут "перекатываться" кости
    sleep = 0  # пауза между перекатываниями
    x = 0
    y = 0
    while count > 0:
        color(count + 7)
        x = random.randint(1, 6)
        y = random.randint(1, 6)
        print(" " * 10, "----- -----")
        print(" " * 10, f"| {x} | | {y} |")
        print(" " * 10, "----- -----")
        time.sleep(sleep)
        sleep += 1 / count
        count -= 1
    return x + y


# Кости
def dice():
    global money      # количество средств на счету игрока
    playGame = True   # маркер главного цикла метода рулетки
    while playGame:
        print()
        color_line(3, "ДОБРО ПОЖАЛОВАТЬ НА ИГРУ В КОСТИ!")
        color(14)
        print(f"\n У тебя на счету {money} {currency}\n")

        color(7)
        rate = get_int_input(0, money, f"    Сделай ставку в пределах {money} {currency}: ")
        if rate == 0:
            return 0

        playRound = True       # игровой цикл - выбрасываем кости, считаем результат, указываем следующую сумму костей
        control = rate       # ставка внутри игры
        oldResult = get_dice()  # хранит сумму костей предыдущей игры
        firstPlay = True       # контролирует - текущий раунд является первым?

        while playRound and rate > 0 and money > 0:

            if rate > money:
                rate = money

            color(11)
            print(f"\n    В твоём распоряжении {rate} {currency}")
            color(12)
            print(f"\n    Текущая сумма чисел на костях: {oldResult}")
            color(11)
            print(f"\n    Сумма чисел на гранях будет больше, меньше или равна предыдущей?")
            color(7)
            x = get_input("0123", "    Введи 1 - больше, 2- меньше, 3 - равна или 0 - выход: ")

            if x != 0:
                firstPlay = False
                if rate > money:
                    rate = money

                money -= rate
                diceResult = get_dice()  # Сумма последнего броска костей

                win = False
                if oldResult > diceResult:
                    if x == "2":
                        win = True
                elif oldResult < diceResult:
                    if x == "1":
                        win = True

                if not x == "3":
                    if win:
                        money += rate + rate // 5
                        victory(rate // 5)
                        rate += rate // 5
                    else:
                        rate = control
                        losing(rate)
                elif x == "3":
                    if oldResult == diceResult:
                        money += rate * 3
                        victory(rate * 2)
                        rate *= 3
                    else:
                        rate = control
                        losing(rate)
                oldResult = diceResult
            else:
                # Если выход на первой ставке
                if firstPlay:
                    money -= rate
                playRound = False


# считаем количество комбинаций цифр OHB
def getMaxCount(digit, v1, v2, v3, v4, v5):
    ret = 0
    if digit == v1:
        ret += 1
    if digit == v2:
        ret += 1
    if digit == v3:
        ret += 1
    if digit == v4:
        ret += 1
    if digit == v5:
        ret += 1
    return ret


# вывод комбинаций цифр OHB
def getOHBRes(rate):
    res = rate
    # создаем переменные для каждой цифры ряда
    d1 = 0
    d2 = 0
    d3 = 0
    d4 = 0
    d5 = 0
    # логические переменные, отвечающие за изменение каждой цифры
    getD1 = True
    getD2 = True
    getD3 = True
    getD4 = True
    getD5 = True
    col = 10

    while (getD1 or
           getD2 or
           getD3 or
           getD4 or
           getD5):

        # начинаем расчёты:
        if getD1:
            d1 += 1
        if getD2:
            d2 -= 1
        if getD3:
            d3 += 1
        if getD4:
            d4 -= 1
        if getD5:
            d5 += 1

        # исключаем двузначные числа
        if d1 > 9:
            d1 = 0
        if d2 < 0:
            d2 = 9
        if d3 > 9:
            d3 = 0
        if d4 < 0:
            d4 = 9
        if d5 > 9:
            d5 = 0

        # условие сброса значения False, чтобы цифры перестали меняться
        if random.randint(0, 20) == 1:
            getD1 = False
        if random.randint(0, 20) == 1:
            getD2 = False
        if random.randint(0, 20) == 1:
            getD3 = False
        if random.randint(0, 20) == 1:
            getD4 = False
        if random.randint(0, 20) == 1:
            getD5 = False

        # меняем цвета цифр
        time.sleep(0.1)
        color(col)
        col += 1
        if col > 15:
            col = 10

        # оформление
        print("    " + "%" * 10)
        print(f"    {d1} {d2} {d3} {d4} {d5}")

    # считаем, сколько цифр совпало
    maxCount = getMaxCount(d1, d1, d2, d3, d4, d5)

    if maxCount < getMaxCount(d2, d1, d2, d3, d4, d5):
        maxCount = getMaxCount(d2, d1, d2, d3, d4, d5)
    if maxCount < getMaxCount(d3, d1, d2, d3, d4, d5):
        maxCount = getMaxCount(d3, d1, d2, d3, d4, d5)
    if maxCount < getMaxCount(d4, d1, d2, d3, d4, d5):
        maxCount = getMaxCount(d4, d1, d2, d3, d4, d5)
    if maxCount < getMaxCount(d5, d1, d2, d3, d4, d5):
        maxCount = getMaxCount(d5, d1, d2, d3, d4, d5)

    # расчёт выигрыша или поражения
    color(14)
    if maxCount == 2:
        print(f" Совпадение двух чисел! Твой выигрыш в размере ставки: {res}")
    elif maxCount == 3:
        res *= 2
        print(f" Совпадение трёх чисел! Твой выигрыш 2:1: {res}")
    elif maxCount == 4:
        res *= 5
        print(f" Совпадение ЧЕТЫРЁХ чисел! Твой выигрыш 5:1: {res}")
    elif maxCount == 5:
        res *= 10
        print(f" БИНГО! Совпадение ВСЕХ чисел! Твой выигрыш 10:1: {res}")
    else:
        losing(res)
        res = 0

    color(11)
    print()
    input(" Нажми ENTER для продолжения...")

    return res


# Однорукий бандит
def one_hand_bandit():
    global money
    playGame = True
    while playGame:
        color_line(3, "ДОБРО ПОЖАЛОВАТЬ НА ИГРУ В ОДНОРУКОГО БАНДИТА!")
        color(14)
        print(f"\n У тебя на счету {money} {currency}\n")
        color(5)
        print(" Правила игры: ")
        print("    1. При совпадении 2-х чисел ставка не списывается.")
        print("    2. При совпадении 3-х чисел выигрыш 2:1.")
        print("    3. При совпадении 4-х чисел выигрыш 5:1.")
        print("    4. При совпадении 5-ти чисел выигрыш 10:0.")
        print("    0. Ставка 0 для завершения игры\n")

        rate = get_int_input(0, money, f"    Введи ставку от 0 до {money}: ")
        if rate == 0:
            return 0

        money -= rate
        money += getOHBRes(rate)

        if money <= 0:
            playGame = False


# пишем метод main_f():
def main_f():
    global money, playGame

    money = load_money()
    startMoney = money

    while playGame and money > 0:
        color_line(10, "Приветствую тебя в нашем казино, дружище!")
        color(14)
        print(f" У тебя на счету {money} {currency}")
        color(6)
        print(" Ты можешь сыграть в:")
        print("    1. Рулетку")
        print("    2. Кости")
        print("    3. Однорукого бандита")
        print("    0. Выход. Ставка 0 в играх - выход.")
        color(7)

        x = get_input("0123", "    Твой выбор? ")

        if x == "0":  # преобразование в цифру будет в функции get_input
            playGame = False
        elif x == "1":
            roulette()
        elif x == "2":
            dice()
        elif x == "3":
            one_hand_bandit()

    color_line(12, "Жаль, что ты покидаешь нас! Но возвращайся скорей")
    color(13)
    if money <= 0:
        print(" Упс, ты остался без денег. Возьми микрокредит и возвращайся!")

    color(11)
    if money > startMoney:
        print("Ну что ж, поздравляем с прибылью!")
        print(f"На начало игры у тебя было {startMoney} {currency}")
        print(f"Сейчас уже {money} {currency}! Играй еще и приумножай!")
    elif money == startMoney:
        print(f"У тебя по прежнему {money} {currency}")
    else:
        print(f"К сожалению ты проиграл {startMoney - money} {currency}")
        print("В следующий развсё обязательно получится!")

    save_money(money)

    input()
    color(7)  # Устанавливаем цвет текста консоли снова в белый
    quit(0)   # Выход с кодом 0 (можно поставить любое другое число)

main_f()