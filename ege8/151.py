sed = set()
k = 0
for s1 in 'ВЛНП':
    for s2 in 'ВЛНП':
        for s3 in 'ВЛНП':
            for s4 in 'ВЛНП':
                if s1 != 'В' and s1 != s3 and s2 != s4:
                    sed.add(s1+s2+s3+s4)
                    k += 1
print(len(sed),k)