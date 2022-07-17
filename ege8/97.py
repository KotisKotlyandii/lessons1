k = 0
for s1 in 'КАЛИЙ':
    for s2 in 'КАЛИЙ':
        for s3 in 'КАЛИЙ':
            for s4 in 'КАЛИЙ':
                for s5 in 'КАЛИЙ':
                    if s1 != "Й" and ("ИАК" not in (s1+s2+s3+s4+s5)) and len(set(s1+s2+s3+s4+s5)) == 5:
                        k += 1
print(k)