k = 0
for s1 in "КРАНТ":
    for s2 in "КРАНТ":
        for s3 in "КРАНТ":
            for s4 in "КРАНТ":
                for s5 in "КРАНТ":
                    if (s1+s2+s3+s4+s5).count('К') == 2:
                        k += 1

print(k)