import os
nums = map(int, os.read(0, os.fstat(0).st_size).split())
n,m = next(nums), next(nums)
nums = [0]+list(nums)
sums = [0]*(n+1)
for i in range(n):
    sums[i+1] = sums[i]+nums[i+1]
dp = [0]*(n+1)
dp[m] = sums[m]
for i in range(m+1, n+1):
    dp[i] = max(dp[i-1]+nums[i],sums[i]-sums[i-m])
os.write(1, str(max(dp)).encode())
os._exit(0)