k = 0
na,ko = 0,0
for s1 in 'АМРТ':
    for s2 in 'АМРТ':
        for s3 in 'АМРТ':
            for s4 in 'АМРТ':
                k += 1
                if s1+s2+s3+s4 == 'МАРТ':
                    na = k
                elif s1+s2+s3+s4 == 'РАМТ':
                    ko = k

print(na,ko)
