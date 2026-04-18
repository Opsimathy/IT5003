n = int(input())
a = [input() for _ in range(n)]
dp = [0] * (n + 1)
nxt = {}
for i in range(n - 1, -1, -1):
    nxt[a[i]] = i + 1
    dp[i] = 1 + min(dp[j] for j in nxt.values())
print(dp[0])
