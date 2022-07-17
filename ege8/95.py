k = 0
for s1 in 'КАБИНЕТ':
    for s2 in 'КАБИНЕТ':
        for s3 in 'КАБИНЕТ':
            for s4 in 'КАБИНЕТ':
                for s5 in 'КАБИНЕТ':
                    for s6 in 'КАБИНЕТ':
                        for s7 in 'КАБИНЕТ':
                            if s1 != 'Б' and ('ЕА' not in s1+s2+s3+s4+s5+s6+s7) and len(set(s1+s2+s3+s4+s5+s6+s7)) == 7:
                                k += 1
print(k)