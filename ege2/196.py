for x in 0, 1:
    for y in 0, 1:
        for z in 0, 1:
            for w in 0, 1:
                f = ((not y or x) or (not z and w)) == (w==x)
                if f:
                    print(x,y,z,w, "|", int(f))
