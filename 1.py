import sys
sys.stdin = open("in.txt")
for _ in range(5):
    hello = list(map(str,input()))
    nysh_clova = ['h','e','l','l','o']
    novoe_hello = ''
    if hello.count('l') >= 2:
        for bykv in hello:
            if bykv in nysh_clova:
                novoe_hello += '{}'.format(bykv)
                nysh_clova.remove(bykv)
        if novoe_hello == "hello":
            print("YES")
        else:
            print("NO")
    else:
        print("NO")