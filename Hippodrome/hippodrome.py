from tkinter import *
from tkinter import messagebox  # формирование отдельного окна с надписью и кнопкой "ОК"
from tkinter import ttk  # выпадающий список

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
    # принимаем сумму средств игрока и возвращаем список значений с шагом 1/10
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

# финансовые показатели
currency = "руб."
money = 0
defaultMoney = 10000

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

# ставки для каждой лошади:
summ01 = IntVar()  # переменные для хранения ставок
summ02 = IntVar()
summ03 = IntVar()
summ04 = IntVar()

# привязываем переменную к виджету:
stavka01["textvariable"] = summ01
stavka02["textvariable"] = summ02
stavka03["textvariable"] = summ03
stavka04["textvariable"] = summ04

# при выборе значения из любого Combobox вызываем метод refreshCombo:
stavka01.bind("<<ComboboxSelected>>", refreshCombo)
stavka02.bind("<<ComboboxSelected>>", refreshCombo)
stavka03.bind("<<ComboboxSelected>>", refreshCombo)
stavka04.bind("<<ComboboxSelected>>", refreshCombo)

refreshCombo("")

stavka01.current(0)
stavka02.current(0)
stavka03.current(0)
stavka04.current(0)




# Выводим главное окно на экран:
root.mainloop()
