def f(a, b):
    if a == b:
        return 1
    elif a > b or a == 28:
        return 0
    return f(a+1, b) + f(a*2, b)

print(f(3, 10) * f(10, 34))

# 56)	Исполнитель Июнь15 преобразует число на экране.
# У исполнителя есть две команды, которым присвоены номера:
# 1. Прибавить 1
# 2. Умножить на 2
# Первая команда увеличивает число на экране на 1, вторая умножает его на 2.
# Программа для исполнителя Июнь15 – это последовательность команд.
# Сколько существует программ, для которых при исходном числе 2 результатом является число 34
# и при этом траектория вычислений содержит число 10 и не содержит число 28?

