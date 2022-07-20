sed = set()
k = 0
for s1 in 'ЧИУАУА':
    for s2 in 'ЧИУАУА':
        for s3 in 'ЧИУАУА':
            for s4 in 'ЧИУАУА':
                for s5 in 'ЧИУАУА':
                    for s6 in 'ЧИУАУА':
                        a = s1+s2+s3+s4+s5+s6
                        if len(set(a)) == 4 and a.count('У') == 2 and a.count('А') == 2:
                            k += 1
                            sed.add(s1+s2+s3+s4+s5+s6)
print(len(sed),k)
print(sed)