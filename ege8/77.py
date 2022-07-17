sed = set()
sog = 'КРБЛК'
glasn = 'ОАИ'
prov1 = lambda a: a[0] in sog and a[1] in glasn and a[2] in sog and a[3] in glasn and a[4] in sog and a[5] in glasn
for s1 in 'ТАРАКАНИЩЕ':
    for s2 in 'ТАРАКАНИЩЕ':
        for s3 in 'ТАРАКАНИЩЕ':
            for s4 in 'ТАРАКАНИЩЕ':
                for s5 in 'ТАРАКАНИЩЕ':
                    for s6 in 'ТАРАКАНИЩЕ':
                        a = s1 + s2 + s3 +s4 +s5 +s6
                        if s1 in sog and len(set(a)) == 6 and prov1(a):
                            sed.add(a)
print(len(sed))