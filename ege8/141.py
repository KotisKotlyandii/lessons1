k = 0
for s1 in 'БЕРКЛИЙ':
    for s2 in 'БЕРКЛИЙ':
        for s3 in 'БЕРКЛИЙ':
            for s4 in 'БЕРКЛИЙ':
                if s1 != 'Й' and (s1+s2+s3+s4).count('Е') + (s1+s2+s3+s4).count('И') > 0:
                    k += 1
print(k)