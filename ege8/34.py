k = 0
n,kon = 0,0
for s1 in 'АЗНС':
    for s2 in 'АЗНС':
        for s3 in 'АЗНС':
            for s4 in 'АЗНС':
                for s5 in 'АЗНС':
                    k += 1
                    print(k,s1+s2+s3+s4+s5)
                    if s1+s2+s3+s4+s5 == 'САЗАН':
                        n = k
                    elif s1+s2+s3+s4+s5 == 'ЗАНАС':
                        kon = k

print(n,kon)
