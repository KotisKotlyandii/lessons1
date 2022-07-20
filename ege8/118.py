def prov(a):
    for i in range(len(a)-1):
        if a[i] == a[i+1]:
            return False
    else:
        return True

k = 0
sed = set()
for s1 in 'АВРОРА':
    for s2 in 'АВРОРА':
        for s3 in 'АВРОРА':
            for s4 in 'АВРОРА':
                for s5 in 'АВРОРА':
                    for s6 in 'АВРОРА':
                        a = s1 + s2 + s3 + s4 + s5 + s6
                        if 'АА' not in a and 'РР' not in a  and len(set(a)) == 4 and a.count('А') == 2 and a.count('Р') == 2:
                            k += 1
                            sed.add(s1+s2+s3+s4+s5+s6)
print(k,len(sed))