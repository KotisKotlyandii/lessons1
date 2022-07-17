k = 0
for s1 in 'КУПЧИХА':
    for s2 in 'КУПЧИХА':
        for s3 in 'КУПЧИХА':
            for s4 in 'КУПЧИХА':
                for s5 in 'КУПЧИХА':
                    for s6 in 'КУПЧИХА':
                        for s7 in 'КУПЧИХА':
                            if len(set(s1+s2+s3+s4+s5+s6+s7)) == 7 and s1 != 'Ч' and ("ИАУ" not in s1+s2+s3+s4+s5+s6+s7):
                                k += 1
print(k)