k = 0
sed = set()
for s1 in 'АВДПР':
    for s2 in 'АВДПР':
        for s3 in 'АВДПР':
            for s4 in 'АВДПР':
                k += 1
                a = s1+s2+s3+s4
                if a.count('А') == 0 and len(set(a)) == 4:
                    print(k,a)