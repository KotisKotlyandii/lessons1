k = 0
sed = set()
for s1 in 'КАЛЬКА':
    for s2 in 'КАЛЬКА':
        for s3 in 'КАЛЬКА':
            for s4 in 'КАЛЬКА':
                for s5 in 'КАЛЬКА':
                    a = s1 + s2 + s3 + s4 + s5
                    if a.count('А') <= 1:
                        k += 1
                        sed.add(a)

print(k, len(sed))
