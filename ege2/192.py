for x in 0,1:
    for y in 0,1:
        for z in 0,1:
            for w in 0,1:
                f =  not (x == (not z)) or ((x or w) == y)
                if not f:
                    print(x,y,z,w,'|', int(f))