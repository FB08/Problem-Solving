# Hyeonseok님 SCC 참고

import sys
from collections import deque
sys.setrecursionlimit(10000)
input = map(int, sys.stdin.read().split())

class SCC: # 완전 연결 요소(Strong Connected Component)
    def __init__(self, graph, n) -> None:
        self.n = n 
        self.graph = graph
        
        self.count = 0 # 최종 구별 연결요소 인덱스
        self.index = 1 #임시 부여용 연결요소 인덱스
        self.sn = [0] * n # 각 정점의 최종 연결요소 인덱스 저장
        self.dfsn = [0] * n # 각 정점의 임시 연결요소 인덱스 저장
        self.finished = [0] * n # dfs의 완료 여부
        self.scc = []
        self.stack = [] #현재 dfs중인 정점
        
        for i in range(n):
            if self.dfsn[i] == 0: #아직 i의 연결요소 인덱스가 정해지지 않았다면
                self.dfs(i)
    
    def dfs(self, vertex):
        self.dfsn[vertex] = self.index
        self.index += 1
        self.stack.append(vertex)


        # 근데 코드를 이렇게 구현해야되나? 이렇게 되면 한 정점에 대해 dfs를 여러번 하게 되는 것 아닌가?
        result = self.dfsn[vertex]
        for nv in self.graph[vertex]: # vertex의 인접 요소들을 모두 방문
            if not self.dfsn[nv]: # 아직 nv의 연결요소 인덱스가 정해지지 않았다면 vertex < nv
                result = min(result, self.dfs(nv)) # result를 nv의 연결요소와 vertex의 연결요소중 가장 작은 값의 인덱스(=가장 큰 범위의 인덱스)로 설정
            elif not self.finished[nv]: # nv의 dfs가 시작되었으나 끝나지 않았으면(=아직 dfsn[nv]가 최소인지 알 수 없음)
                # 양방향 또는 cycle을 형성함을 의미한다. a가 b를 호출했고 중간 과정을 거쳐 결과적으로 b가 다시 a를 호출함을 의미
                # = a와 b가 방문할할 수 있는 정점은 같다.
                result = min(result, self.dfsn[nv]) # 따라서 일단 현재의 인덱스를 비교한다. 어차피 a가 갈곳은 b도 가기에 정확한 값을 알지 않아도 된다.

        
        if result == self.dfsn[vertex]: # 자신이 해당요소의 첫번째 정점이라면
            # 자신보다 밑에 있는 stack에 위치한다는건 
            scc = [] # 새로운 연결요소집합 만들기 
            while self.stack: # vertex보다 나중에 호출된 정점들(하나의 연결요소 집합) -> 순환 사이클이 형성된(양방향 인접한) 
                top = self.stack.pop()
                self.sn[top] = self.count # top의 최종 인덱스 저장
                self.finished[top] = 1 # top의 dfs상태를 끝내기
                if top == vertex: # vertex까지만 양방향 연결됨
                    break
            
            self.count += 1 # 연결계수 
            self.scc.append(scc)
        
        return result

def solve():
    n, m = next(input), next(input)
    graph = [[] for _ in range(n)]
    
    for _ in range(m):
        a, b = next(input), next(input)
        graph[a].append(b)
    
    scc = SCC(graph, n)
    sccgraph = [[] for _ in range(scc.count)] # 정점별 방문할 수 있는 연결요소 리스트
    for i in range(n):
        for nv in graph[i]: # i의 인접 정점 방문
            if scc.sn[i] != scc.sn[nv]: # 같은 연결요소가 아니라면 리스트에 추가
                sccgraph[scc.sn[i]].append(scc.sn[nv])
    
    visited = {}
    for i in range(scc.count): # 연결요소에 대해 BFS
        visited[i] = [0] * scc.count
        visited[i][i] = 1
        queue = deque([i])
        while queue:
            vertex = queue.popleft()
            
            for nv in sccgraph[vertex]:
                if not visited[i][nv]:
                    visited[i][nv] = 1
                    queue.append(nv)
    
    q = next(input)
    for _ in range(q):
        s, e = next(input), next(input)
        print(visited[scc.sn[s]][scc.sn[e]])

solve()
