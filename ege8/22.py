k = 0
for s1 in 'КОТ':
    for s2 in 'КОТ':
        for s3 in 'КОТ':
            for s4 in 'КОТ':
                for s5 in 'КОТ':
                    if (s1+s2+s3+s4+s5).count('О') == 2:
                        k += 1

print(k)
