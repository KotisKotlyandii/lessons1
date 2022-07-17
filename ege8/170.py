sed = set()
k = 0
for s1 in 'ЖАЛЕЙ':
    for s2 in 'ЖАЛЕЙ':
        for s3 in 'ЖАЛЕЙ':
            for s4 in 'ЖАЛЕЙ':
                for s5 in 'ЖАЛЕЙ':
                    a = s1+s2+s3+s4+s5
                    if a.count('Й') <= 1 and s1 != 'Й' and s5 != 'Й' and ('ЙЕ' not in a) and ('ЕЙ' not in a):
                        sed.add(a)
                        k += 1
print(len(sed),k)