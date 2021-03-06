from tkinter import *
from tkinter import messagebox  # формирование отдельного окна с надписью и кнопкой "ОК"
from tkinter import ttk  # выпадающий список
from random import randint  # теперь вместо random.randint(x, y) можно писать просто randint(x, y)

# ************************************************************
# Отсюда будем писать методы и функции
# ************************************************************


def horsePlaceInWindow():
    # Расположение дошадей на экране
    horse01.place(x=int(x01), y=20)
    horse02.place(x=int(x02), y=100)
    horse03.place(x=int(x03), y=180)
    horse04.place(x=int(x04), y=260)


def insertText(s):
    # добавляем строку в чат
    textDiary.insert(INSERT, s + "\n")
    textDiary.see(END)


def loadMoney():
    # Чтение из файла оставшейся суммы
    try:
        f = open("money.dat", "r")
        m = int(f.readline())
        f.close()
    except FileNotFoundError:
        print(f"Файла не существует, задано значение {defaultMoney} {currency}")
        m = defaultMoney
    return m


def saveMoney(moneyToSave):
    # запись суммы в файл
    try:
        f = open("money.dat", "w")
        f.write(str(moneyToSave))
        f.close()
    except:
        print("Ошибка создания файла, наш Ипподром закрывается!")
        quit(0)


def getValues(summa):
    """
    принимаем сумму средств игрока
    и возвращаем список значений с шагом 1/10 для Combobox
    """
    value = []
    if summa > 9:
        for i in range(0, 11):
            value.append(i * (int(summa) // 10))
    else:
        value.append(0)
        if summa > 0:
            value.append(summa)

    return value


def refreshCombo(eventObject):
    # Подсчёт оставшейся суммы при ставках
    summ = summ01.get() + summ02.get() + summ03.get() + summ04.get()
    labelAllMoney["text"] = f"У Вас на счету: {int(money - summ)} {currency}."

    stavka01["values"] = getValues(int(money - summ02.get() - summ03.get() - summ04.get()))
    stavka02["values"] = getValues(int(money - summ01.get() - summ03.get() - summ04.get()))
    stavka03["values"] = getValues(int(money - summ02.get() - summ01.get() - summ04.get()))
    stavka04["values"] = getValues(int(money - summ02.get() - summ03.get() - summ01.get()))

    # включаем или выключаем кнопку 'Старт'
    if summ > 0:
        startButton["state"] = "normal"
    else:
        startButton["state"] = "disabled"

    # включаем/выключаем чекбоксы:
    if summ01.get() > 0:
        horse01Game.set(True)
    else:
        horse01Game.set(False)

    if summ02.get() > 0:
        horse02Game.set(True)
    else:
        horse02Game.set(False)

    if summ03.get() > 0:
        horse03Game.set(True)
    else:
        horse03Game.set(False)

    if summ04.get() > 0:
        horse04Game.set(True)
    else:
        horse04Game.set(False)


def runHorse():
    # при нажатии на кнопку 'Старт' (запрещаем пользователю изменения при забеге):
    global money
    startButton["state"] = "disabled"
    stavka01["state"] = "disabled"
    stavka02["state"] = "disabled"
    stavka03["state"] = "disabled"
    stavka04["state"] = "disabled"
    # со средств списывается сумма ставки:
    money -= summ01.get() + summ02.get() + summ03.get() + summ04.get()
    moveHorse()


def problemHorse():
    # случайное событие неправильного поведения лошадей
    global reverse01, reverse02, reverse03, reverse04
    global play01, play02, play03, play04
    global fastSpeed01, fastSpeed02, fastSpeed03, fastSpeed04

    # выбираем лошадь для события
    horse = randint(1, 4)
    # чем выше число, тем ниже вероятность события
    maxRand = 10000
    if horse == 1 and play01 == True and x01 > 0:
        if randint(0, maxRand) < (state01 * 5):
            # маркер движения в обратный:
            reverse01 = not reverse01
            # сообщение пользователю в чате:
            messagebox.showinfo("Аааааа!", f"Лошадь {nameHorse01} развернулась и бежит в другую сторону!")
        elif randint(0, maxRand) < (state01 * 5):
            # лошадь остановилась
            play01 = False
            messagebox.showinfo("Никогда такого не было и вот опять ", f"{nameHorse01} заржала и скинула жокея!")
        elif randint(0, maxRand) < (state01 * 5) and not fastSpeed01:
            messagebox.showinfo("Великолепно! ", f"{nameHorse01} перестал притворяться и ускорился!")
            # лошадь ускоряется
            fastSpeed01 = True
    elif horse == 2 and play02 == True and x02 > 0:
        if randint(0, maxRand) < (state02 * 5):
            reverse02 = not reverse02
            messagebox.showinfo("Аааааа!", f"Лошадь {nameHorse02} развернулась и бежит в другую сторону!")
        elif randint(0, maxRand) < (state02 * 5):
            play02 = False
            messagebox.showinfo("Никогда такого не было и вот опять ", f"{nameHorse02} заржала и скинула жокея!")
        elif randint(0, maxRand) < (state02 * 5) and not fastSpeed02:
            messagebox.showinfo("Великолепно! ", f"{nameHorse02} перестал притворяться и ускорился!")
            # лошадь ускоряется
            fastSpeed02 = True
    elif horse == 3 and play03 == True and x03 > 0:
        if randint(0, maxRand) < (state03 * 5):
            reverse03 = not reverse03
            messagebox.showinfo("Аааааа!", f"Лошадь {nameHorse03} развернулась и бежит в другую сторону!")
        elif randint(0, maxRand) < (state03 * 5):
            play03 = False
            messagebox.showinfo("Никогда такого не было и вот опять ", f"{nameHorse03} заржала и скинула жокея!")
        elif randint(0, maxRand) < (state03 * 5) and not fastSpeed03:
            messagebox.showinfo("Великолепно! ", f"{nameHorse03} перестал притворяться и ускорился!")
            # лошадь ускоряется
            fastSpeed03 = True
    elif horse == 4 and play04 == True and x04 > 0:
        if randint(0, maxRand) < (state04 * 5):
            reverse04 = not reverse04
            messagebox.showinfo("Аааааа!", f"Лошадь {nameHorse04} развернулась и бежит в другую сторону!")
        elif randint(0, maxRand) < (state04 * 5):
            play04 = False
            messagebox.showinfo("Никогда такого не было и вот опять ", f"{nameHorse04} заржала и скинула жокея!")
        elif randint(0, maxRand) < (state04 * 5) and not fastSpeed01:
            messagebox.showinfo("Великолепно! ", f"{nameHorse04} перестал притворяться и ускорился!")
            # лошадь ускоряется
            fastSpeed04 = True


def moveHorse():
    # Движение лошади
    global x01, x02, x03, x04

    # вызов метода problemHorse() с вероятностью в 20%:
    if randint(0, 100) < 20:
        problemHorse()

    # hfcxbnsdftv crjhjcnm lkz rf;ljq kjiflb
    speed01 = (randint(1, timeDay + weather) + randint(1, int(7 - state01) * 3)) / randint(10, 175)
    speed02 = (randint(1, timeDay + weather) + randint(1, int(7 - state02) * 3)) / randint(10, 175)
    speed03 = (randint(1, timeDay + weather) + randint(1, int(7 - state03) * 3)) / randint(10, 175)
    speed04 = (randint(1, timeDay + weather) + randint(1, int(7 - state04) * 3)) / randint(10, 175)

    multiple = 3
    speed01 *= int(randint(1, 2 + state01) * (1 + fastSpeed01 * multiple))
    speed02 *= int(randint(1, 2 + state02) * (1 + fastSpeed02 * multiple))
    speed03 *= int(randint(1, 2 + state03) * (1 + fastSpeed03 * multiple))
    speed04 *= int(randint(1, 2 + state04) * (1 + fastSpeed04 * multiple))

    # вправо или влево бежит лошадь:
    if play01:
        if not reverse01:
            x01 += speed01
        else:
            x01 -= speed01
    if play02:
        if not reverse02:
            x02 += speed02
        else:
            x02 -= speed02
    if play03:
        if not reverse03:
            x03 += speed03
        else:
            x03 -= speed03
    if play04:
        if not reverse04:
            x04 += speed04
        else:
            x04 -= speed04

    horsePlaceInWindow()

    # текущая ситуация
    allPlay = play01 or play02 or play03 or play04  # проверяем движется ли лошадь
    allX = x01 < 0 and x02 < 0 and x03 < 0 and x04 < 0  # лошади за пределами окна
    allReverse = reverse01 and reverse02 and reverse03 and reverse04  # бегут ли лошади назад
    if not allPlay or allX or allReverse:  # если выполняются следующие условия
        winRound(0)                        # вызвать метод... и передать аргумент...
        return 0                           # прекратить выполнение метода moveHorse()

    # Если координата < 952 (это расположение поля финиша на изображении),
    # то заново вызываем метод moveHorse с интервалом в 5 миллисекунд.
    # (Получается что-то типа рекурсии).
    if (x01 < 952 and
       x02 < 952 and
       x03 < 952 and
       x04 < 952):
        root.after(5, moveHorse)  # root.after(TIME_MS, METHOD)
    else:
        if x01 >= 952:
            winRound(1)
        elif x02 >= 952:
            winRound(2)
        elif x03 >= 952:
            winRound(3)
        elif x04 >= 952:
            winRound(4)


def viewWeather():
    # о погоде в чате
    s = "Сейчас на ипподроме "
    if timeDay == 1:
        s += "ночь, "
    elif timeDay == 2:
        s += "утро, "
    elif timeDay == 3:
        s += "день, "
    elif timeDay == 4:
        s += "вечер, "

    if weather == 1:
        s += "льёт сильный дождь."
    elif weather == 2:
        s += "моросит дождик."
    elif weather == 3:
        s += "облачно, на горизонте тучи."
    elif weather == 4:
        s += "безоблачно, ветер."
    elif weather == 5:
        s += "безоблачно, прекрасная погода!"
    insertText(s)


def getHealth(name, state, win):
    # сюда отправляем имя, состояние и коэф.выигрыша каждой лошади
    s = f"Лошадь {name} "
    if state == 5:
        s += "мучается несварением желудка."
    elif state == 4:
        s += "плохо спала. Подёргивается веко."
    elif state == 3:
        s += "сурова и беспощадна."
    elif state == 2:
        s += "в отличном настроении, покушала хорошо."
    elif state == 1:
        s += "просто ракета!"

    s += f" ({win}:1)"
    return s


def healthHorse():
    # выводим в чат строку о лошадях
    insertText(getHealth(nameHorse01, state01, winCoeff01))
    insertText(getHealth(nameHorse02, state02, winCoeff02))
    insertText(getHealth(nameHorse03, state03, winCoeff03))
    insertText(getHealth(nameHorse04, state04, winCoeff04))


def setupHorse():
    # установка состояния лошадей и погоды на предстартовый уровень
    # (можно всё загнать в метод, в том числе при первом запуске!)
    global state01, state02, state03, state04
    global weather, timeDay
    global winCoeff01, winCoeff02, winCoeff03, winCoeff04
    global play01, play02, play03, play04
    global reverse01, reverse02, reverse03, reverse04
    global fastSpeed01, fastSpeed02, fastSpeed03, fastSpeed04

    weather = randint(1, 5)
    timeDay = randint(1, 4)

    state01 = randint(1, 5)
    state02 = randint(1, 5)
    state03 = randint(1, 5)
    state04 = randint(1, 5)

    winCoeff01 = int(100 + randint(1, 30 + state01 * 60)) / 100
    winCoeff02 = int(100 + randint(1, 30 + state02 * 60)) / 100
    winCoeff03 = int(100 + randint(1, 30 + state03 * 60)) / 100
    winCoeff04 = int(100 + randint(1, 30 + state04 * 60)) / 100

    # маркеры ситуаций:
    reverse01 = False
    reverse02 = False
    reverse03 = False
    reverse04 = False

    play01 = True
    play02 = True
    play03 = True
    play04 = True

    fastSpeed01 = False
    fastSpeed02 = False
    fastSpeed03 = False
    fastSpeed04 = False


def winRound(horse):
    # победа лошади
    global x01, x02, x03, x04, money

    res = "К финишу пришла лошадь "  # res - результат
    if horse == 1:
        res += nameHorse01
        win = summ01.get() * winCoeff01
    elif horse == 2:
        res += nameHorse02
        win = summ02.get() * winCoeff02
    elif horse == 3:
        res += nameHorse03
        win = summ03.get() * winCoeff03
    elif horse == 4:
        res += nameHorse04
        win = summ04.get() * winCoeff04

    if horse > 0:
        res += f"! Вы выиграли {int(win)} {currency}. "
        if win > 0:
            res += "Поздравляем! Средства уже зачислены на Ваш счёт!"
            insertText(f"Этот забег принёс Вам {int(win)} {currency}.")
        else:
            res += "К сожалению, Ваша лошадь была неправильной. Попробуйте ещё раз!"
            insertText("Делайте ставку! Увеличивайте прибыль!")
        messagebox.showinfo("РЕЗУЛЬТАТ", res)
    else:
        messagebox.showinfo("Всё плохо", "До финиша не дошёл никто.\
        Забег признан несостоявшимся. Все ставки возвращены.")
        win = summ01.get() + summ02.get() + summ03.get() + summ04.get()

    money += win
    saveMoney(int(money))

    # сброс переменных
    setupHorse()

    # сбрасываем виджеты (можно оформить отдельным методом)
    startButton["state"] = "normal"
    stavka01["state"] = "readonly"
    stavka02["state"] = "readonly"
    stavka03["state"] = "readonly"
    stavka04["state"] = "readonly"
    stavka01.current(0)
    stavka02.current(0)
    stavka03.current(0)
    stavka04.current(0)

    # сбрасываем координаты на начальные и перерисовываем методом horsePlaceInWindow()
    x01 = 20
    x02 = 20
    x03 = 20
    x04 = 20
    horsePlaceInWindow()

    # обновляем интерфейс
    refreshCombo(eventObject="")  # Обновляет выпадающие списки и чекбоксы
    viewWeather()
    healthHorse()
    insertText(f"Ваши средства: {int(money)} {currency}.")
    if money < 1:
        messagebox.showinfo("Стоп!", "На ипподром без средств заходить нельзя!")
        quit(0)


# создаем переменную (нашего окна), и передаем ей управление библиотекой:
root = Tk()

# ************************************************************
# Отсюда определим значения переменных
# ************************************************************

# размеры окна программы:
WIDTH = 1024
HEIGHT = 600

# Позиции (координаты x) для лошадей:
x01 = 20
x02 = 20
x03 = 20
x04 = 20

# клички лошадей:
nameHorse01 = "Хлыст"
nameHorse02 = "Бродяга"
nameHorse03 = "Халкер"
nameHorse04 = "Прожорливый"

# маркеры ситуаций:
# отвечает за направление лошади
reverse01 = False
reverse02 = False
reverse03 = False
reverse04 = False
# перемещается ли лошадь?
play01 = True
play02 = True
play03 = True
play04 = True
# ускорение лошади
fastSpeed01 = False
fastSpeed02 = False
fastSpeed03 = False
fastSpeed04 = False

# финансовые показатели
currency = "руб."
money = 0
defaultMoney = 10000

# погода (1 - ливень, ураган; 5 - ясная погода)
weather = randint(1, 5)

# время суток (1 - ночь, 2 - утро, 3 - день, 4 - вечер)
timeDay = randint(1, 4)

# Состояние лошадей:
# (1 - великолепно, 5 - ужасно больна)
state01 = randint(1, 5)
state02 = randint(1, 5)
state03 = randint(1, 5)
state04 = randint(1, 5)

# коэффициент выигрышана основе показателя здоровья лошади
winCoeff01 = int(100 + randint(1, 30 + state01 * 60)) / 100
winCoeff02 = int(100 + randint(1, 30 + state02 * 60)) / 100
winCoeff03 = int(100 + randint(1, 30 + state03 * 60)) / 100
winCoeff04 = int(100 + randint(1, 30 + state04 * 60)) / 100

# ************************************************************
# Отсюда организуем формирование элементов в окне
# ************************************************************

# Создаём главное окно
# вычисляем координаты для размещения окна по центру экрана
POS_X = root.winfo_screenwidth() // 2 - WIDTH // 2
POS_Y = root.winfo_screenheight() // 2 - HEIGHT // 2
# где root.winfo_screenwidth вычисляет размеры экрана

# установка заголовка
root.title("ИППОДРОМ")

# запрещаем изменение размеров окна (ширина, высота)
root.resizable(False, False)

# устанавливаем ширину, высоту и позицию
root.geometry(f"{WIDTH}x{HEIGHT}+{POS_X}+{POS_Y}")

# виджет PhotoImage хранит изображение
# виджет Label отрисовывает изображения:
road_image = PhotoImage(file="road.png")  # загружаем изображение фона в виджет PhotoImage
road = Label(root, image=road_image)      # устанавливаем изображение в виджет Label
road.place(x=0, y=17)                     # выводим Label изображение в окно, задав координаты

horse01_image = PhotoImage(file="horse01.png")
horse01 = Label(root, image=horse01_image)

horse02_image = PhotoImage(file="horse02.png")
horse02 = Label(root, image=horse02_image)

horse03_image = PhotoImage(file="horse03.png")
horse03 = Label(root, image=horse03_image)

horse04_image = PhotoImage(file="horse04.png")
horse04 = Label(root, image=horse04_image)

# Сразу выводим их на экран:
horsePlaceInWindow()

# кнопка "Старт"
startButton = Button(text="СТАРТ", font="arial 20", width=61, background="#37AA37")
startButton.place(x=20, y=370)
# где - width - ширина кнопки;
#     - background - цвет кнопки в 16-ричном представлении
startButton["state"] = "disabled"  # делаем виджет кнопки 'Старт' неактивным

# Информационный чат
textDiary = Text(width=70, height=8, wrap=WORD)  # wrap - перенос строки по словам
textDiary.place(x=430, y=450)

# прикрепляем к тексту полосу прокрутки
scroll = Scrollbar(command=textDiary.yview, width=20)  # yview - привязка ползункаик оси y
scroll.place(x=990, y=450, height=132)
textDiary["yscrollcommand"] =scroll.set

# загружаем сумму средств игрока из файла
money = loadMoney()

# Если игрок беден и несчастен, выгоняем его
if money <= 0:
    messagebox.showinfo("Стоп!", "На ипподром без средств заходить нельзя!")
    quit(0)

labelAllMoney = Label(text=f"Осталось средств: {money} {currency}.", font="Arian 12")
labelAllMoney.place(x=20, y=565)

# информация о лошадях:
labelHorse01 = Label(text="Ставка на лошадь #1")
labelHorse01.place(x=20, y=450)

labelHorse02 = Label(text="Ставка на лошадь #2")
labelHorse02.place(x=20, y=480)

labelHorse03 = Label(text="Ставка на лошадь #3")
labelHorse03.place(x=20, y=510)

labelHorse04 = Label(text="Ставка на лошадь #4")
labelHorse04.place(x=20, y=540)

# чекбоксы для лошадок:
horse01Game = BooleanVar()  # логическая переменная
horse01Game.set(0)          # по умолчанию - 0
horseCheck01 = Checkbutton(text=nameHorse01, variable=horse01Game, onvalue=1, offvalue=0)
# создаем чеквокс и привязяваем к переменной (variable)
horseCheck01.place(x=150, y=448)

horse02Game = BooleanVar()
horse02Game.set(0)
horseCheck02 = Checkbutton(text=nameHorse02, variable=horse02Game, onvalue=1, offvalue=0)
horseCheck02.place(x=150, y=478)

horse03Game = BooleanVar()
horse03Game.set(0)
horseCheck03 = Checkbutton(text=nameHorse03, variable=horse03Game, onvalue=1, offvalue=0)
horseCheck03.place(x=150, y=508)

horse04Game = BooleanVar()
horse04Game.set(0)
horseCheck04 = Checkbutton(text=nameHorse04, variable=horse04Game, onvalue=1, offvalue=0)
horseCheck04.place(x=150, y=538)

# запрещаем пользователю изменять значения чекбоксов
horseCheck01["state"] = "disabled"
horseCheck02["state"] = "disabled"
horseCheck03["state"] = "disabled"
horseCheck04["state"] = "disabled"

# выпадающий список:
stavka01 = ttk.Combobox(root)
stavka02 = ttk.Combobox(root)
stavka03 = ttk.Combobox(root)
stavka04 = ttk.Combobox(root)

stavka01["state"] = "readonly"
stavka01.place(x=280, y=450)

stavka02["state"] = "readonly"
stavka02.place(x=280, y=480)

stavka03["state"] = "readonly"
stavka03.place(x=280, y=510)

stavka04["state"] = "readonly"
stavka04.place(x=280, y=540)

# ставки для каждой лошади (значения из Combobox):
summ01 = IntVar()  # переменные для хранения ставок
summ02 = IntVar()
summ03 = IntVar()
summ04 = IntVar()

# привязываем переменную к виджету Combobox:
stavka01["textvariable"] = summ01
stavka02["textvariable"] = summ02
stavka03["textvariable"] = summ03
stavka04["textvariable"] = summ04

# при выборе значения из любого Combobox вызываем метод refreshCombo:
stavka01.bind("<<ComboboxSelected>>", refreshCombo)
stavka02.bind("<<ComboboxSelected>>", refreshCombo)
stavka03.bind("<<ComboboxSelected>>", refreshCombo)
stavka04.bind("<<ComboboxSelected>>", refreshCombo)

# обновляем значения Combobox:
refreshCombo("")

# устанавливаем самое первое значение списка:
stavka01.current(0)  # по умолчанию - "0"
stavka02.current(0)
stavka03.current(0)
stavka04.current(0)

# назначаем метод выполняющийся при нажатии на кнопку "СТАРТ"
startButton["command"] = runHorse

viewWeather()
healthHorse()

# Выводим главное окно на экран:
root.mainloop()
