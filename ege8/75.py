k = 0
prov1 = lambda a: len([i for i in range(0,len(a),2) if a[i] in sog]) == 3 and len([i for i in range(1,len(a),2) if a[i] in glasn]) == 3
sed = set()
sog = 'КРБЛК'
glasn = 'ОАИ'
for s1 in 'КОРАБЛИК':
    for s2 in 'КОРАБЛИК':
        for s3 in 'КОРАБЛИК':
            for s4 in 'КОРАБЛИК':
                for s5 in 'КОРАБЛИК':
                    for s6 in 'КОРАБЛИК':
                        a = s1 + s2 + s3 + s4 +s5 + s6
                        if s1 in sog and len(set(a)) == 6 and prov1(a):
                            sed.add(a)
print(len(sed))
print(sed)