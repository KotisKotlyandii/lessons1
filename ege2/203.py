for x in 0,1:
    for y in 0,1:
        for z in 0,1:
            for w in 0,1:
                f = ((not x or w) or y and not z) and ((not y or not z) or x and not w)
                if not f:
                    print(z,w,y,x,'|', int(f))