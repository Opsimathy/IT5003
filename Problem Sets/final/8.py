from collections import deque
n, m = map(int, input().split())
d = {'English': 0} | {s: i + 1 for i, s in enumerate(input().split())}
g = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b, c = input().split()
    u, v, c = d[a], d[b], int(c)
    g[u].append((v, c))
    g[v].append((u, c))
dist = [-1] * (n + 1)
dist[0] = 0
q = deque([0])
while q:
    u = q.popleft()
    for v, _ in g[u]:
        if dist[v] < 0:
            dist[v] = dist[u] + 1
            q.append(v)
print('Impossible' if -1 in dist else sum(min(c for u, c in g[v] if dist[u] == dist[v] - 1) for v in range(1, n + 1)))
