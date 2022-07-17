k = 0
sed = set()
for s1 in 'БАНКИР':
    for s2 in 'БАНКИР':
        for s3 in 'БАНКИР':
            for s4 in 'БАНКИР':
                for s5 in 'БАНКИР':
                    for s6 in 'БАНКИР':
                        a = s1 + s2 + s3 + s4 + s5 + s6
                        if a.count('А') <= 1 and a.count('И') <= 1:
                            k += 1
                            sed.add(a)

print(k, len(sed))
