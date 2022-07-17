k = 0
for s1 in 'АГОР':
    for s2 in 'АГОР':
        for s3 in 'АГОР':
            for s4 in 'АГОР':
                k += 1
                if "А" not in (s1+s2+s3+s4):
                    print(k)