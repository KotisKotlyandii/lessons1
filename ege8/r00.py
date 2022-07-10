k = 0
for s1 in "УОА":
    for s2 in "УОА":
        for s3 in "УОА":
            for s4 in "УОА":
                for s5 in "УОА":
                    s = s1+s2+s3+s4+s5
                    k += 1
                    if k == 240:
                        print(k, s)

