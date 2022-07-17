k = 0
for s1 in 'ПАНЕЛЬ':
    for s2 in 'ПАНЕЛЬ':
        for s3 in 'ПАНЕЛЬ':
            for s4 in 'ПАНЕЛЬ':
                for s5 in 'ПАНЕЛЬ':
                    for s6 in 'ПАНЕЛЬ':
                        if s1 != "Ь" and ("ЕАП" not in (s1+s2+s3+s4+s5)) and len(set(s1+s2+s3+s4+s5+s6)) == 6:
                            k += 1
print(k)