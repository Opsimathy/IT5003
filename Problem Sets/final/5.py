from heapq import heappush, heappop
n, m = map(int, input().split())
g = [[] for _ in range(n + 1)]
for _ in range(m):
    u, v = map(int, input().split())
    g[u].append(v)
    g[v].append(u)
army = [0] + [int(input()) for _ in range(n)]
seen = [False] * (n + 1)
seen[1] = True
ans = army[1]
q = []
for v in g[1]:
    heappush(q, (army[v], v))
while q and q[0][0] < ans:
    _, u = heappop(q)
    if seen[u]:
        continue
    seen[u] = True
    ans += army[u]
    for v in g[u]:
        if not seen[v]:
            heappush(q, (army[v], v))
print(ans)
