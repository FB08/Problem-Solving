import sys
input = sys.stdin.readline
n = int(input())
dp = [0] * n
numbers = list(map(int, input().split()))
for i in range(n):
    dp[i] = max(dp[i-1]+numbers[i], numbers[i])
print(max(dp))
