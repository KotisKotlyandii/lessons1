k = 0
for s1 in 'АВБГДЯ':
    for s2 in 'АВБГД':
        for s3 in 'АВБГД':
            for s4 in 'АВБГДЯ':
                if (s1+s2+s3).count('Я') <= 1:
                    k += 1
print(k)