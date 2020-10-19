a = int(input())
spic = []
for _ in range(a):
    element = int(input())
    spic.append(element)
for j in range(len(spic)):
    for i in range(1, len(spic)):
        if sum(map(int,str(spic[i - 1]))) > sum(map(int,str(spic[i]))):
            spic[i], spic[i - 1] = spic[i - 1], spic[i]
        if sum(map(int,str(spic[i - 1]))) == sum(map(int,str(spic[i]))):
            if spic[i-1] > spic[i]:
                spic[i], spic[i - 1] = spic[i - 1], spic[i]

print(spic)