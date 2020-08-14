import simple_draw as sd

# Нарисовать стену из кирпичей. Размер кирпича - 100х50
# Использовать вложенные циклы for
line1 = 600
line_in_if = 0
line_in_if_2 = 50
line_in_else = 50
line_in_else_2 = 100
y1 = 50
x = 100
x1 = 70
for line in range(1,13):
    sd.line(start_point = sd.get_point(0,line1), end_point = sd.get_point(600,line1),color = sd.COLOR_ORANGE, width= 3)
    line1 -= 50
    if line % 2 == 1:
        for i in range(6):
            sd.line(start_point=sd.get_point(x, line_in_if), end_point=sd.get_point(x, line_in_if_2), color=sd.COLOR_ORANGE, width=3)
            x += 100
    else:
        for i in range(7):
            sd.line(start_point = sd.get_point(x1,line_in_else), end_point=sd.get_point(x1,line_in_else_2), color=sd.COLOR_ORANGE, width=3)
            x1 += 85
        x = 100
        x1 = 70
        line_in_if += 100
        line_in_if_2 += 100
        line_in_else += 100
        line_in_else_2 += 100


sd.pause()
