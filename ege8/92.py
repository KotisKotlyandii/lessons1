k = 0
for s1 in 'МАНОК':
    for s2 in 'МАНОК':
        for s3 in 'МАНОК':
            for s4 in 'МАНОК':
                for s5 in 'МАНОК':
                    if s1 != 'О' and 'АО' not in s1+s2+s3+s4+s5 and len(set(s1+s2+s3+s4+s5)) == 5:
                        k += 1
print(k)