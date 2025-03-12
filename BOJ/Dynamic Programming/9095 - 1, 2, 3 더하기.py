def solution():
    import os
    import sys
    _, *input = map(int, sys.stdin.read().split())
    # _, *input = map(int, os.read(0, os.fstat(0).st_size).split())
    n = max(input)
    dp = [0, 1, 2, 4]
    for i in range(4, n+1):
        dp.append(dp[i-1]+dp[i-2]+dp[i-3])
    for k in input:
        os.write(1, (str(dp[k])+'\n').encode())
    os._exit(0)

solution()