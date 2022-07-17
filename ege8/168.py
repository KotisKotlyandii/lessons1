sed = set()
k = 0
for s1 in 'КЛЕЙ':
    for s2 in 'КЛЕЙ':
        for s3 in 'КЛЕЙ':
            for s4 in 'КЛЕЙ':
                for s5 in 'КЛЕЙ':
                    for s6 in 'КЛЕЙ':
                        a = s1+s2+s3+s4+s5+s6
                        if a.count('Й') <= 1 and s1 != 'Й' and s6 != 'Й' and ('ЙЕ' not in a) and ('ЕЙ' not in a):
                            sed.add(a)
                            k += 1
print(len(sed),k)