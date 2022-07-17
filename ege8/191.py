k = 0
sed = set()
for s1 in 'САЛЬСА':
    for s2 in 'САЛЬСА':
        for s3 in 'САЛЬСА':
            for s4 in 'САЛЬСА':
                for s5 in 'САЛЬСА':
                    for s6 in 'САЛЬСА':
                        a = s1 + s2 + s3 + s4 + s5 + s6
                        if a.count('А') <= 1:
                            k += 1
                            sed.add(a)

print(k, len(sed))
