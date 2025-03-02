def solution():
    import os
    input = map(int, os.read(0, os.fstat(0).st_size).split())
    a, b = next(input), next(input)
    G = [set(), set()] # [안자람, 자람]
    for x in range(b):
        for y in range(a):
            k = next(input)
            if k != -1:
                G[k].add((x, y))
    day = 0
    while G[1] and G[0]:
        day += 1
        temp = []
        while G[1]:
            x = G[1].pop()
            for a,b in [(0,1),(0,-1),(1,0),(-1,0)]:
                y = (x[0]+a, x[1]+b)
                if y in G[0]:
                    G[0].discard(y)
                    temp.append(y)
        G[1] = temp
    os.write(1, str(-1 if G[0] else day).encode())
    os._exit(0)
solution()
        