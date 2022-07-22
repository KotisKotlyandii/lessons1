for x in range(int(input())):
    a = input()
    b = input()
    if len(a) == 1 and a != b:
        print("NO")
    elif len(a) == 1 and a == b:
        print('YES')
    else:
        for i in range(len(a)):
            if a[i] != b:
                a = a.replace(a[i],'_',1)
        a = a.replace('__','')
        if len(a) == 1 and a == b or len(a) // 2 < a.count(b):
            print('YES')
        else:
            print('NO')