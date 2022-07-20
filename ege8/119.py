k = 0
for s1 in 'МАГИСТР':
    for s2 in 'МАГИСТР':
        for s3 in 'МАГИСТР':
            for s4 in 'МАГИСТР':
                for s5 in 'МАГИСТР':
                    a = s1+s2+s3+s4+s5
                    if len(set(a)) == 5 and a.count('А') + a.count("И") <= 1:
                        k += 1
print(k)