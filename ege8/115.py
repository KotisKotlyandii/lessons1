def prov(a):
    for i in range(len(a)-1):
        if a[i] == a[i+1]:
            return False
    else:
        return True

k = 0
sed = set()
for s1 in 'МАРТА':
    for s2 in 'МАРТА':
        for s3 in 'МАРТА':
            for s4 in 'МАРТА':
                for s5 in 'МАРТА':
                    a = s1+s2+s3+s4+s5
                    if  'АА' not in a and len(set(a)) == 4 and a.count('А') == 2 :
                        k += 1
                        sed.add(s1+s2+s3+s4+s5)
print(k,len(sed))