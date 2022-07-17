sed = set()
k = 0
for s1 in '1234':
    for s2 in '01234':
        for s3 in '01234':
            for s4 in '01234':
                for s5 in '01234':
                    for s6 in '01234':
                        if int(s1+s2+s3+s4+s5+s6) % 2 == 0 and s1 == '3':
                            k += 1
                            sed.add(s1+s2+s3+s4+s5+s6)
print(len(sed),k)