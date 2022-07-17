k = 0
for s1 in 'АВГЕН':
    for s2 in 'АВГЕН':
        for s3 in 'АВГЕН':
            for s4 in 'АВГЕН':
                k += 1
                if "А" not in (s1+s2+s3+s4):
                    print(k)