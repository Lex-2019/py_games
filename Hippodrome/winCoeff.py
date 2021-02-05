# тестируем значение выигрыша

from random import randint

# Состояние лошадей:
# (1 - великолепно, 5 - ужасно больна)
state01 = 1
state02 = 2
state03 = 4
state04 = 5

# коэффициент выигрышана основе показателя здоровья лошади
# (чем ниже показатель stateXX тем ниже коэф. выигрыша)
# (формулу конечно, можно составить свою)
winCoeff01 = int(100 + randint(1, 30 + state01 * 60)) / 100
winCoeff02 = int(100 + randint(1, 30 + state02 * 60)) / 100
winCoeff03 = int(100 + randint(1, 30 + state03 * 60)) / 100
winCoeff04 = int(100 + randint(1, 30 + state04 * 60)) / 100

print(f"""winCoeff01 = {winCoeff01}
winCoeff02 = {winCoeff02}
winCoeff03 = {winCoeff03}
winCoeff04 = {winCoeff04}""")