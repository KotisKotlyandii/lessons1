sed = set()
k = 0
for s1 in 'ДЖОБС':
    for s2 in 'ДЖОБС':
        for s3 in 'ДЖОБС':
            for s4 in 'ДЖОБС':
                for s5 in 'ДЖОБС':
                    for s6 in 'ДЖОБС':
                        a = s1+s2+s3+s4+s5+s6
                        if a.count('Д') == 1 and a.count('О') == 1 and a.count('С') == 1 and a.count('Ж') <= 2:
                            sed.add(a)
                            k += 1
print(len(sed),k)