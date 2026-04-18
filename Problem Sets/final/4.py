n = int(input())
g = [input() for _ in range(10)]
dp = [[0] * 10 for _ in range(n)]
for r in range(10):
    dp[-1][r] = g[r][-1] == '.'
for c in range(n - 2, -1, -1):
    for r in range(10):
        if g[r][c] == '.':
            dp[c][r] = dp[c + 1][min(9, r + 1)] or dp[c + 1][max(0, r - 1)]
r = 9
a = []
for c in range(n - 1):
    d = min(9, r + 1)
    u = max(0, r - 1)
    if dp[c + 1][d]:
        a.append(0)
        r = d
    else:
        a.append(1)
        r = u
ans = []
i = 0
while i < n - 1:
    if a[i]:
        j = i
        while j < n - 1 and a[j]:
            j += 1
        ans.append((i, j - i))
        i = j
    else:
        i += 1
print(len(ans))
for i in ans:
    print(*i)
