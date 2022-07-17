k = 0
for s1 in 'АВГДИНОР':
    for s2 in 'АВГДИНОР':
        for s3 in 'АВГДИНОР':
            for s4 in 'АВГДИНОР':
                k += 1
                if s1+s2 == 'ИР':
                    print(k)