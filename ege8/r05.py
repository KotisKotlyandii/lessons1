k = 0
for s1 in "ACGT":
    for s2 in "ACGT":
        for s3 in "ACGT":
            for s4 in "ACGT":
                for s5 in "ACGT":
                    if (s1+s2+s3+s4+s5).count('A') == 2:
                        k += 1

print(k)