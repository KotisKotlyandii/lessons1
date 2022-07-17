k = 0
sed = set()
for s1 in 'БАЛОН':
    for s2 in 'БАЛОН':
        for s3 in 'БАЛОН':
            for s4 in 'БАЛОН':
                for s5 in 'БАЛОН':
                    for s6 in 'БАЛОН':
                        a = s1+s2+s3+s4+s5+s6
                        if a.count('А') <= 1 and a.count('О') <= 1:
                            k += 1
                            sed.add(a)
                            
print(k,len(sed))
