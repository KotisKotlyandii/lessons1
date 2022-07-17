k = 0
sed = set()
for s1 in 'САКУРА':
    for s2 in 'САКУРА':
        for s3 in 'САКУРА':
            for s4 in 'САКУРА':
                for s5 in 'САКУРА':
                    a = s1 + s2 + s3 + s4 + s5
                    if a.count('А') <= 1 and a.count('У') <= 1:
                        k += 1
                        sed.add(a)

print(k, len(sed))
