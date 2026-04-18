from heapq import heappush, heappop
while True:
    n, m, a, k = map(int, input().split())
    if n == m == a == k == 0:
        break
    g = [[] for _ in range(n + 1)]
    for _ in range(m):
        u, v, w = map(int, input().split())
        g[u].append((v, w))
        g[v].append((u, w))
    dist = [k] * (n + 1)
    un = 0
    for _ in range(a):
        start = int(input())
        pq = [(0, start)]
        while pq:
            d, u = heappop(pq)
            if d >= dist[u] or d >= k:
                continue
            if dist[u] == k:
                un += 1
            dist[u] = d
            for v, w in g[u]:
                nd = d + w
                if nd < dist[v] and nd < k:
                    heappush(pq, (nd, v))
        print(n - un)
    print()
