k = 0
prov1 = lambda a: a[0] in glasn and a[1] in sog and a[2] in glasn and a[3] in sog and a[4] in glasn and a[5] in sog
sed = set()
sog = 'КРБЛК'
glasn = 'ОАИ'
for s1 in 'КОРАБЛИКИ':
    for s2 in 'КОРАБЛИКИ':
        for s3 in 'КОРАБЛИКИ':
            for s4 in 'КОРАБЛИКИ':
                for s5 in 'КОРАБЛИКИ':
                    for s6 in 'КОРАБЛИКИ':
                        a = s1 + s2 + s3 + s4 +s5 + s6
                        if s1 in glasn and len(set(a)) == 6 and prov1(a):
                            sed.add(a)
                            print(a)
print(len(sed))