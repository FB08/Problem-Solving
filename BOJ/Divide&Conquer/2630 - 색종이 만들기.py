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
  
