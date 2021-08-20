raspol = list(map(str,input()))

chel_in_pod = 0
posled_chel = '1'
est_li_opasn = False
bul_povtor = False

for chel in raspol:
    if chel_in_pod == 7:
        print("YES")
        est_li_opasn = True
        bul_povtor = True
        break
    elif chel == posled_chel:
        chel_in_pod += 1
    elif chel != posled_chel:
        posled_chel = chel
        chel_in_pod = 1

if chel_in_pod == 7 and bul_povtor == False:
    print("YES")
    est_li_opasn = True

if est_li_opasn == False:
    print("NO")
