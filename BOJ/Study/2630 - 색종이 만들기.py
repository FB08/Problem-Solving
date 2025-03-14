def solution():
    import sys
    input = sys.stdin.readline
    n = int(input())
    paper = [list(map(int, input().split())) for _ in range(n)]
    def solve(x, y, l):
        if l == 1:
            return (0, 1) if paper[x][y] else (1, 0)

        result = [0, 0]

        for i in [x, x+l//2]:
            for j in [y, y+l//2]:
                r = solve(i, j, l//2)
                result[0] += r[0]
                result[1] += r[1]
        
        if not result[0]:
            return (0, 1)
        if not result[1]:
            return (1, 0)
        return tuple(result)
    ans = solve(0, 0, n)
    sys.stdout.write('\n'.join(map(str, ans)))

solution()

# 첫 제출 코드와는 다르게 sum을 이용하지 않아서 온전히 분할정복으로 문제를 해결함
# 불필요한 재귀 호출을 줄였으며 시간복잡도 O(n)
