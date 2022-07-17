k = 0
n,kon = 0,0
for s1 in 'ОПРТ':
    for s2 in 'ОПРТ':
        for s3 in 'ОПРТ':
            for s4 in 'ОПРТ':
                for s5 in 'ОПРТ':
                    k += 1
                    if s1+s2+s3+s4+s5 == 'ТОПОР':
                        n = k
                    elif s1+s2+s3+s4+s5 == 'РОПОТ':
                        kon = k

print(n-kon+2)

