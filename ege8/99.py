k = 0
for s1 in 'НИЧЬЯ':
    for s2 in 'НИЧЬЯ':
        for s3 in 'НИЧЬЯ':
            for s4 in 'НИЧЬЯ':
                for s5 in 'НИЧЬЯ':
                    if s1 != "Ь" and ("ЬИЯ" not in (s1+s2+s3+s4+s5)) and len(set(s1+s2+s3+s4+s5)) == 5:
                        k += 1
print(k)