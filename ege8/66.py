k = 0
for s1 in 'abcdefghijklmnopqrstuvwxyz':
    for s2 in 'abcdefghijklmnopqrstuvwxyz':
        for s3 in 'abcdefghijklmnopqrstuvwxyz':
            for s4 in 'abcdefghijklmnopqrstuvwxyz':
                if (s1+s2+s3+s4) == (s1+s2+s3+s4)[::-1]:
                    k += 1
        
print(k)