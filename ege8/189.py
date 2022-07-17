k = 0
sed = set()
for s1 in 'КОРНЕТ':
    for s2 in 'КОРНЕТ':
        for s3 in 'КОРНЕТ':
            for s4 in 'КОРНЕТ':
                for s5 in 'КОРНЕТ':
                    a = s1 + s2 + s3 + s4 + s5
                    if a.count('О') <= 1 and a.count('Е') <= 1:
                        k += 1
                        sed.add(a)

print(k, len(sed))
