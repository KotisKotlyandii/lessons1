k = 0
for s1 in 'РУСТАМ':
    for s2 in 'РУСТАМ':
        for s3 in 'РУСТАМ':
            for s4 in 'РУСТАМ':
                for s5 in 'РУСТАМ':
                    for s6 in 'РУСТАМ':
                        a = s1+s2+s3+s4+s5+s6
                        if a.count('Р') + a.count('С') + a.count('Т') + a.count('М') >= 3:
                            k += 1
print(k)