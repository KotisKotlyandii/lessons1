k = 0
for s1 in 'abcdefghijklmnopqrstuvwxyz':
    for s2 in 'abcdefghijklmnopqrstuvwxyz':
        for s3 in 'abcdefghijklmnopqrstuvwxyz':
            for s4 in 'abcdefghijklmnopqrstuvwxyz':
                for s5 in 'abcdefghijklmnopqrstuvwxyz':
                    for s6 in 'abcdefghijklmnopqrstuvwxyz':
                            if (s1 + s2 + s3 + s4 + s5 + s6) == (s1 + s2 + s3 + s4 + s5 + s6)[::-1]:
                                k += 1

print(k)