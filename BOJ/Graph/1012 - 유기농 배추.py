import sys
from collections import deque
input = map(int, sys.stdin.read().split())


for _ in range(next(input)):
    w, h = next(input), next(input)
    G = [(next(input), next(input)) for _ in range(next(input))]
    visited = [[0]*h for _ in range(w)]

    def dfs(i):
        for j, k in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            x, y = i[0]+j, i[1] + k
            if (x,y) in G and not visited[x][y]:
                visited[x][y] = 1
                q.append((x, y))

    for i in range(len(G)):
        x = G[i]
        if not visited[x[0]][x[1]]:
            q = deque([x])
            dfs(x)