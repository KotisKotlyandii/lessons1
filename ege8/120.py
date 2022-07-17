k = 0
for s1 in 'ПРИКАЗ':
    for s2 in 'ПРИКАЗ':
        for s3 in 'ПРИКАЗ':
            for s4 in 'ПРИКАЗ':
                a = s1+s2+s3+s4
                if len(set(a)) == 4 and  a.count('А') + a.count("И") <= 1 :
                     k += 1
print(k)