a = ['-5']*200
b = [a.copy() for _ in range(200)]

for x in range(1,200):
    for y in range(1,200):
        if x + y >= 79:
            b[x][y] = '0'

for x in range(1,200):
    for y in range(1,200):
        if b[x][y] == '-5':
            if b[x+3][y] == '0' or b[x][y+3] == "0" or b[x*2][y] == "0" or b[x][y*2] == "0":
                b[x][y] = "1"

for x in range(1,200):
    for y in range(1,200):
        if b[x][y] == "-5":
            if b[x+3][y] == "1" and b[x][y+3] == "1" and b[x*2][y] == "1" and b[x][y*2] == "1":
                b[x][y] = "2"
for x in range(1,200):
    for y in range(1,200):
        if b[x][y] == "-5":
            if b[x+3][y] == "2" or b[x][y+3] == "2" or b[x*2][y] == "2" or b[x][y*2] == "2":
                b[x][y] = "3"
for x in range(1,200):
    for y in range(1,200):
        if b[x][y] == "-5":
            if b[x+3][y] in "13" and b[x][y+3] in "13" and b[x*2][y] in "13" and b[x][y*2] in "13":
                b[x][y] = "4"
for i in range(1, 200):
    print(*b[i][1:], sep="\t")