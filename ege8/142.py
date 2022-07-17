k = 0
for s1 in 'ВАЯЮЩИЙ':
    for s2 in 'ВАЯЮЩИЙ':
        for s3 in 'ВАЯЮЩИЙ':
            for s4 in 'ВАЯЮЩИЙ':
                a = s1+s2+s3+s4
                if s1 != 'Й' and a.count('А') + a.count('Я') + a.count('Ю') + a.count('И') > 0:
                    k += 1
print(k)