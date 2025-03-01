def solution():
    import os
    input = map(int, os.read(0, os.fstat(0).st_size).split())
    G = [[] for _ in range(next(input)+1)]
    for _ in range(next(input)):
        a, b = next(input), next(input)
        G[a].append(b)
        G[b].append(a)
    visit = [0]*len(G)
    q = [1]
    result,visit[1] = 0, 1
    while q:
        x = q.pop()
        for y in G[x]:
            if not visit[y]: 
                q.append(y)
                visit[y] = 1
                result += 1
    os.write(1, str(result).encode())
    os._exit(0)
solution()