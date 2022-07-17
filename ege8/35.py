k = 0
n,kon = 0,0
for s1 in 'ДКМО':
    for s2 in 'ДКМО':
        for s3 in 'ДКМО':
            for s4 in 'ДКМО':
                for s5 in 'ДКМО':
                    k += 1
                    if s1+s2+s3+s4+s5 == 'ДОМОК':
                        n = k
                    elif s1+s2+s3+s4+s5 == 'КОМОД':
                        kon = k

print(n,kon)
