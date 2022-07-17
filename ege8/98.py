k = 0
for s1 in 'ГЕЛИЙ':
    for s2 in 'ГЕЛИЙ':
        for s3 in 'ГЕЛИЙ':
            for s4 in 'ГЕЛИЙ':
                for s5 in 'ГЕЛИЙ':
                    if s1 != "Й" and ("ИЕЙ" not in (s1+s2+s3+s4+s5)) and len(set(s1+s2+s3+s4+s5)) == 5:
                        k += 1
print(k)