def solution():
    import sys
    input = sys.stdin.readline
    n, m = map(int, input().split())
    arr = []
    for _ in range(n):
        arr.append(list(map(lambda x: [0, -1, 0][int(x)], input().split())))
        if 2 in arr[-1]:
            start = (n, arr[-1].index(2))
    # bfs
    visit = [[0]*m for _ in range(m)]
    q = [start]
    while q:
        x = q.pop(0)
        r = arr[x[0]][x[1]]+1
        for i,j in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            a,b = x[0]+i, x[1]+j
            if arr[a][b] and not visit[a][b]:
                arr[a][b] = r
                q.append((a, b))

    for i in range(n):
        sys.stdout.write(' '.join(map(str, arr[n]))+'\n')

solution()
    