sed = set()
for s1 in 'АБК':
    for s2 in 'АБК':
        for s3 in 'АБК':
            for s4 in 'АБК':
                s = s1+s2+s3+s4
                if s.count("АА")==0 and len(set(s)) == 3 and s.count("А")==2:
                    sed.add(s1+s2+s3+s4)
print(len(sed))