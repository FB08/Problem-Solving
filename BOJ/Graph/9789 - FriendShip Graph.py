import sys
from collections import deque

input = map(int, sys.stdin.read().split())

v, e = next(input), next(input)
G = [[] for _ in range(v)]
for _ in range(e):
  G[next(input)].append(next(input))

visit = {i:[0*v] for i in range(v)}
for i in range(v):
  visit[i][i] = 1
  queue = deque([i])
  while queue:
    x = queue.popleft()
    for k in G[x]:
      if visit[i][k]: continue
      visit[i][k] = 1
      queue.extend(G[k])

for _ in range(next(input)):
    print(visit[next(input)][next(input)])

# HyeonSeok님 코드 참고
