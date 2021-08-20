import random

kol_resh = 0
obs_resh = 0
neprav_resh = 0

while True:
    chislo_1 = random.randrange(1, 10)
    chislo_2 = random.randrange(1, 10)
    primer = int(input("Cколько будет {} умножить на {}? - ".format(chislo_1,chislo_2)))

    if primer == 0:
        print("Правильных ответов -", kol_resh)
        print("Неправильвых ответов -", neprav_resh)
        print("Всего задач -", obs_resh)
        break
    if primer == chislo_1 * chislo_2:
        print("Правильно!")
        kol_resh += 1
        obs_resh += 1
    else:
        print("""Неправильно!
Правильный ответ""", chislo_1*chislo_2)
        neprav_resh += 1
        obs_resh += 1
