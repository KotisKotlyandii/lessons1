k = 0
for s1 in 'АБВГДЕ':
    for s2 in 'АБВДЕ':
        for s3 in 'АБВДЕ':
            for s4 in 'АБВГДЕ':
                if (s1+s2+s3+s4).count('Г') == 1:
                    k += 1
print(k)