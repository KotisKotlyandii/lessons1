k = 0
for s1 in 'КРОЙ':
    for s2 in 'КРОЙ':
        for s3 in 'КРОЙ':
            for s4 in 'КРОЙ':
                if s1 != 'Й' and 'ОЙ' not in s1+s2+s3+s4 and len(set(s1+s2+s3+s4)) == 4:
                    k += 1
print(k)