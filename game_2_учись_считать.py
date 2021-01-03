# переменные для ввчислений:
lowDigit = 10      # нижняя граница
highDigit = 100    # верхняя граница
sign = 0           # знак операции
answer = 0         # искомое значение в примере
firstNumber = 0    # первое значение в примере
secondNumber = 0   # второе значение в примере
x = 0              # переменная коэффициента

# переменные для статистики:
score = 0          # очки
countTask = 0      # количество решённых примеров
rightAnswer = 0    # количество правильных ответов
playGame = True    # главный цикл

# ========================================

print("""Компьютер составляет пример. Введите ответ.
Для завершения работы введите STOP""")
print("*" * 40)

while playGame:
    print(f"Ваши очки: {score}")
    print(f"Обработано задач: {countTask}")
    print(f"Правильных ответов: {rightAnswer}")
    print("-" * 20 + "\n")
    # print("Желаете выбрать арифметические действия, или предоставите выбор компьютеру?")

    import random

    sign = random.randint(0, 3)
    # 0 - плюс
    # 1 - минус
    # 2 - умножить
    # 3 - делить

    # ******************** СЛОЖЕНИЕ
    if sign == 0:
        answer = random.randint(lowDigit, highDigit)
        secondNumber = random.randint(lowDigit, answer)
        firstNumber = answer - secondNumber
        if random.randint(0, 1) == 0:
            print(f"{firstNumber} + {secondNumber} = ?")
        else:
            print(f"{secondNumber} + {firstNumber} = ?")

    # ******************** ВЫЧИТАНИЕ
    elif sign == 1:
        firstNumber = random.randint(lowDigit, highDigit)
        secondNumber = random.randint(0, firstNumber - lowDigit)
        answer = firstNumber - secondNumber
        print(f"{firstNumber} - {secondNumber} = ?")

    # ******************** УМНОЖЕНИЕ
    elif sign == 2:
        x = random.randint(1, (highDigit - lowDigit) // random.randint(1, highDigit // 10) + 1)
        firstNumber = random.randint(1, (highDigit - lowDigit) // x + 1)
        secondNumber = random.randint(lowDigit, highDigit) // firstNumber
        if secondNumber == 0:
            secondNumber = 1
        answer = firstNumber * secondNumber
        print(f"{firstNumber} * {secondNumber} = ?")

    # ******************* ДЕЛЕНИЕ
    elif sign == 3:
        x = random.randint(1, (highDigit - lowDigit) // random.randint(1, highDigit // 10) + 1)
        firstNumber = random.randint(1, (highDigit - lowDigit) // x + 1)
        secondNumber = random.randint(lowDigit, highDigit) // firstNumber
        if secondNumber == 0:
            secondNumber = 1
        firstNumber = firstNumber * secondNumber
        answer = firstNumber // secondNumber
        print(f"{firstNumber} / {secondNumber} = ?")

    # ожидаем ввода цыфры либо команды STOP на латинице или кирилице
    user = ""
    while (not user.isdigit()
           and user.upper() != "STOP"
           and user.upper() != "S"
           and user.upper() != "Ы"
           and user.upper() != "ЫЕЩЗ"):
        user = input("\nВаш ответ? ")

        # анализируем введенный ответ:
        if (user.upper() == "HELP"
                or user == "?"
                or user == ","
                or user.upper() == "РУДЗ"):
            if answer > 9:
                print(f"Последняя цифра ответа: {answer % 10}")
            else:
                print("Ответ состоит из одной цифры, подсказка невозможна.")
            score -= 10

        # Команда STOP
        elif (user.upper() == "STOP"
              or user.upper() == "S"
              or user.upper() == "Ы"
              or user.upper() == "ЫЕЩЗ"):
            playGame = False

        # проверка на ввод числа:
        elif not user.isdigit():
            print("\nВведите, пожалуйста, число.\n")

        else:
            # счетчик обработанных вопросов
            countTask += 1
            if int(user) == answer:
                print("\nПравильно!\n")
                rightAnswer += 1
                score += 10
            else:
                print(f"\nОтвет неправильный... Правильно: {answer}")
                print(f"вы можете ввести команду HELP или ? чтобы увидеть последнюю цыфру ответа (-10 очков)\n")
                score -= 20

# Прощальные строки по окончании игры:
print("*" * 45)
print("СТАТИСТИКА ИГРЫ:")
print(f"Всего примеров: {countTask}")
print(f"Правильных ответов: {rightAnswer}")
print(f"Неправильных ответов: {countTask - rightAnswer}")
if countTask > 0:
    print(f"Процент верных ответов: {int(rightAnswer / countTask * 100)}%")
else:
    print("Процент верных ответов : 0%")
print("Возвращайтесь!")

print("*" * 40)
input("Нажмите Enter для выхода...")
quit()
