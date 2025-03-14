def solution():
  import os
  import sys
  input = sys.stdin.readline
  n = int(input())
  arr = []
  for _ in range(n):
    arr.append(list(map(int, input().split())))

  result = [0, 0]
  
  def DC(l, x, y):
    r = sum([sum(arr[i][y:y+l]) for i in range(x, x+l)])
    if r in [0, l**2]:
      result[[0, l**2].index(r)] += 1
      return
    for i in [x, x+l//2]:
      for j in [y, y+l//2]:
        DC(l//2, i, j)
    return
  DC(n, 0, 0)
  os.write(1, (str(result[0])+'\n'+str(result[1])).encode())
  os._exit(0)

solution()

# 이 코드의 단점
# 분할정복을 완전히 이용하지 않고 sum을 중복적으로 이용하여 실행시간이 더 오래걸림
# 재귀 깊이가 logn정도이고 각 실행에 n^2이 걸리므로 시간복잡도가 약 O(n^2logn)
