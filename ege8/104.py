k = 0
for s1 in 'НАДПИСЬ':
    for s2 in 'НАДПИСЬ':
        for s3 in 'НАДПИСЬ':
            for s4 in 'НАДПИСЬ':
                for s5 in 'НАДПИСЬ':
                    for s6 in 'НАДПИСЬ':
                        for s7 in 'НАДПИСЬ':
                            if len(set(s1+s2+s3+s4+s5+s6+s7)) == 7 and s1 != 'Ь' and ("ЬИА" not in s1+s2+s3+s4+s5+s6+s7):
                                k += 1
print(k)