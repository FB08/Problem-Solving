def solution():
    import os
    import sys
    input = sys.stdin.readline # 메모리를 위해 한줄씩 입력받음
    for _ in range(int(input())):
        W, H, K = map(int, input().split())
        G = set() # x in G연산을 빠르게 하기 위해 set이용
        for _ in range(K):
            x,y = map(int, input().split())
            G.add((x, y)) 

        result = 0
        while G: # bfs로 연결요소의 개수를 구함
            result += 1
            q = [G.pop()]
            while q:
                x = q.pop()
                for a,b in [(0,1),(0,-1),(1,0),(-1,0)]:
                    y = (x[0]+a, x[1]+b)
                    if y in G:
                        G.discard(y)
                        q.append(y)

        os.write(1, (str(result)+'\n').encode())
    os._exit(0)

solution()

#===========[ Python 자료 구조 ]==========
# for문에서 가장 빠르고 메모리가 적은 구조: list
# x in arr에서 가장 빠른 구조: dict, set (hash이용)

