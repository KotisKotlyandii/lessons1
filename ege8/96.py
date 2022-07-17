k = 0
for s1 in 'КОМБАЙН':
    for s2 in 'КОМБАЙН':
        for s3 in 'КОМБАЙН':
            for s4 in 'КОМБАЙН':
                for s5 in 'КОМБАЙН':
                    for s6 in 'КОМБАЙН':
                        for s7 in 'КОМБАЙН':
                            if s1 != 'Й' and ('АЙ' not in s1+s2+s3+s4+s5+s6+s7) and len(set(s1+s2+s3+s4+s5+s6+s7)) == 7:
                                k += 1
print(k)