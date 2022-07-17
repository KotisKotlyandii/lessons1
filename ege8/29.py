k = 0
for s1 in "КАНТ":
    for s2 in "КАНТ":
        for s3 in "КАНТ":
            for s4 in "КАНТ":
                for s5 in "КАНТ":
                    for s6 in "КАНТ":
                        if (s1+s2+s3+s4+s5+s6).count('К') == 2:
                            k += 1

print(k)