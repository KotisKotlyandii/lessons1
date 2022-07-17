sed = set()
k = 0
for s1 in 'ОБЪЕМ':
    for s2 in 'ОБЪЕМ':
        for s3 in 'ОБЪЕМ':
            for s4 in 'ОБЪЕМ':
                if (s1+s2+s3+s4).count('О') == 1 and s1 != 'Ъ' and s4 != 'Ъ':
                    sed.add(s1+s2+s3+s4)
                    k += 1
print(len(sed),k)