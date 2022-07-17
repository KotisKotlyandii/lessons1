k = 0
for s1 in 'ШАНЕЛЬ':
    for s2 in 'ШАНЕЛЬ':
        for s3 in 'ШАНЕЛЬ':
            for s4 in 'ШАНЕЛЬ':
                for s5 in 'ШАНЕЛЬ':
                    for s6 in 'ШАНЕЛЬ':
                        if len(set(s1+s2+s3+s4+s5+s6)) == 6 and s1 != 'Ь' and ("ЕАЬ" not in s1+s2+s3+s4+s5+s6):
                            k += 1
print(k)