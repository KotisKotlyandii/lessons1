# -*- coding: utf-8 -*-

# (цикл while)

# Ежемесячная стипендия студента составляет educational_grant руб., а расходы на проживание превышают стипендию
# и составляют expenses руб. в месяц. Рост цен ежемесячно увеличивает расходы на 3%, кроме первого месяца
# Составьте программу расчета суммы денег, которую необходимо единовременно попросить у родителей,
# чтобы можно было прожить учебный год (10 месяцев), используя только эти деньги и стипендию.
# Формат вывода:
#   Студенту надо попросить ХХХ.ХХ рублей

educational_grant, expenses = 10000, 12000
months = 10
all_moths = 0
help_parents = 0
while months > all_moths:
    all_moths += 1
    if all_moths == 1:
        help_parents = expenses - educational_grant
        continue
    else:
        expenses = expenses + ( expenses * 0.03 )
        help_parents = help_parents + (expenses - educational_grant)
print("студенту надо попросить {} рублей".format(int(help_parents)))

