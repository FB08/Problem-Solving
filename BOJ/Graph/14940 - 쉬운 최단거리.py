def solution():
    import sys
    input = sys.stdin.readline
    n, m = map(int, input().split())
    arr = []
    for i in range(n):
        arr.append([[0, -1, 2][int(x)] for x in input().split()])
        if 2 in arr[-1]:
            start = (i, arr[-1].index(2))
    # bfs
    visit = [[0]*m for _ in range(n)]
    arr[start[0]][start[1]] = 0
    q = [start]
    while q:
        x = q.pop(0)
        r = arr[x[0]][x[1]]+1
        for i,j in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            a,b = x[0]+i, x[1]+j
            if a<0 or b<0 or a==m or b==n: continue
            if arr[a][b] and not visit[a][b]:
                arr[a][b] = r
                visit[a][b] = 1
                q.append((a, b))

    for i in range(n):
        sys.stdout.write(' '.join(map(str, arr[i]))+'\n')

solution()
    