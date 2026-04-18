for _ in range(int(input())):
    n, m = map(int, input().split())
    c = [i - 1 for i in map(int, input().split())]
    g = [[] for _ in range(n)]
    d = [0] * n
    for _ in range(m):
        u, v = (int(i) - 1 for i in input().split())
        g[u].append(v)
        d[v] += 1

    def f(s):
        deg = d[:]
        q = [[], []]
        for i in range(n):
            if deg[i] == 0:
                q[c[i]].append(i)
        cur = s
        done = res = 0
        while done < n:
            while q[cur]:
                u = q[cur].pop()
                done += 1
                for v in g[u]:
                    deg[v] -= 1
                    if deg[v] == 0:
                        q[c[v]].append(v)
            if done < n:
                cur ^= 1
                res += 1
        return res
    print(min(f(0), f(1)))
