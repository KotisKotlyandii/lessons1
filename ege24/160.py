t = input()

t = t.replace('XYZ', 'A')

spisok = list(map(str,t.split()))
vtor = []
for i in spisok:
    if i[0] in "XYZ" and i[-1] in "XYZ" and ('X' not in t[1:-1] and 'Y' not in t[1:-1] and 'Z' not in t[1:-1]):
        vtor.append(len(vtor[1:-1])*3+2)

print(max(vtor))