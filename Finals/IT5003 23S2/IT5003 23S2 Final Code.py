def solve(n, e, k):
    if k >= 2:
        return sum(w for _, _, w in e)
    g = [[] for _ in range(n + 1)]
    for u, v, w in e:
        g[u].append((v, w))
        g[v].append((u, w))

    def f(start):
        s = [(start, 0, 0)]
        bn = start
        bd = 0
        while s:
            u, p, d = s.pop()
            if d > bd:
                bd = d
                bn = u
            for v, w in g[u]:
                if v != p:
                    s.append((v, u, d + w))
        return bn, bd
    return f(f(1)[0])[1]


n = 6
e = [(1, 2, 3), (2, 3, 1), (1, 4, 7), (1, 5, 9), (5, 6, 5)]
print(solve(n, e, 7))
print(solve(n, e, 1))
