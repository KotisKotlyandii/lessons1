for a in 0, 1:
    for b in 0, 1:
        for c in 0, 1:
                f = ((a == b) or (not b or c))
                if f:
                    print(a,b,c, "|", int(f))
