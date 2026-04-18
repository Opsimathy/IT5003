# Matric Number: A0332008U
# Name: Li Jiaru
# Lab Group Number: B3B
# Lab TA Name: Manish Choudhary

from sys import setrecursionlimit
setrecursionlimit(1 << 20)
n, m, q = map(int, input().split())
g = [[] for _ in range(n + 1)]
c, v, t = [-1] * (n + 1), [], 0
def dfs(a, t):
    for b, f in g[a]:
        v[t] |= f
        if c[b] == -1:
            c[b] = t
            dfs(b, t)
for _ in range(m):
    a, b, f = map(int, input().split())
    g[a].append((b, f))
    g[b].append((a, f))
for i in range(n + 1):
    if c[i] == -1:
        c[i] = t
        v.append(0)
        dfs(i, t)
        t += 1
for _ in range(q):
    a, b = map(int, input().split())
    print(v[c[a]].bit_count() if c[a] == c[b] else -1)
