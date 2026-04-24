from typing import List, Tuple


class Solution:
    def shortestPath(self, N: int, s: int, t: int) -> int:
        def near(u):
            if u % 3 == 0:
                return [(u // 3, 0)]
            x = u // 3
            return [(x, 1), (x + 1, 1)]
        return min(ca + 2 * abs(a - b) + cb for a, ca in near(s)
                                            for b, cb in near(t))

    def shortestPathMissing(self, N: int, s: int, t: int,
                            miss: List[Tuple[int, int]]) -> float:
        from math import inf
        missing = {tuple(sorted(e)) for e in miss}

        def gone(u, v):
            return tuple(sorted((u, v))) in missing

        def near(u):
            x = u // 3
            if u % 3 == 0:
                return [(x, 0)]
            ans = []
            if not gone(u, 3 * x):
                ans.append((x, 1))
            if x + 1 <= N and not gone(u, 3 * (x + 1)):
                ans.append((x + 1, 1))
            return ans

        def dist(a, b):
            lo, hi = min(a, b), max(a, b)
            return inf if any(lo <= x < hi for x in bad) else 2 * (hi - lo)
        bad = set()
        for u, v in missing:
            i = min(u, v) // 3
            if i < N:
                a, b, c, d = 3 * i, 3 * i + 1, 3 * i + 2, 3 * i + 3
                if (gone(a, b) or gone(b, d)) and (gone(a, c) or gone(c, d)):
                    bad.add(i)
        ans = min(ca + dist(a, b) + cb for a, ca in near(s) for b, cb in near(t))
        return -1 if ans == inf else ans

    def alternativeShortestPath(self, n: int, edges: List[Tuple[int, int, int]],
                                s: int, t: int) -> int:
        from heapq import heappush, heappop
        from math import inf
        graph = [[] for _ in range(n)]
        rev = [[] for _ in range(n)]
        for i, (u, v, w) in enumerate(edges):
            graph[u].append((v, w, i))
            rev[v].append((u, w, i))

        def dijkstra(start, adj):
            dist = [inf] * n
            dist[start] = 0
            pq = [(0, start)]
            while pq:
                d, u = heappop(pq)
                if d != dist[u]:
                    continue
                for v, w, _ in adj[u]:
                    if d + w < dist[v]:
                        dist[v] = d + w
                        heappush(pq, (dist[v], v))
            return dist

        S = dijkstra(s, graph)
        if S[t] == inf:
            return -1
        T = dijkstra(t, rev)
        shortest = S[t]
        removed = set()
        for i, (u, v, w) in enumerate(edges):
            if S[u] + w + T[v] == shortest:
                removed.add(i)
        dist = [inf] * n
        dist[s] = 0
        pq = [(0, s)]
        while pq:
            d, u = heappop(pq)
            if u == t:
                return d
            if d != dist[u]:
                continue
            for v, w, i in graph[u]:
                if i in removed:
                    continue
                if d + w < dist[v]:
                    dist[v] = d + w
                    heappush(pq, (dist[v], v))
        return -1


tests = [[2, 0, 6], [2, 1, 5], [4, 0, 12], [4, 2, 10]]
for t in tests:
    print(f"{t} -> {Solution().shortestPath(*t)}")
"""[2, 0, 6] -> 4
[2, 1, 5] -> 2
[4, 0, 12] -> 8
[4, 2, 10] -> 6"""

tests = [[2, 0, 6, [(0, 1)]], [2, 0, 6, [(0, 1), (0, 2)]],
         [2, 0, 6, [(3, 4), (5, 6)]], [2, 0, 6, [(3, 4)]]]
for t in tests:
    print(f"{t} -> {Solution().shortestPathMissing(*t)}")
"""[2, 0, 6, [(0, 1)]] -> 4
[2, 0, 6, [(0, 1), (0, 2)]] -> -1
[2, 0, 6, [(3, 4), (5, 6)]] -> -1
[2, 0, 6, [(3, 4)]] -> 4"""

tests = [[7, [[0, 1, 1], [1, 2, 2], [2, 6, 1],
              [0, 3, 1], [3, 6, 4], [0, 4, 2],
              [4, 6, 2], [0, 5, 3], [5, 6, 4]], 0, 6],
         [7, [[0, 1, 1], [1, 2, 2], [2, 6, 1],
              [0, 3, 1], [3, 6, 4], [0, 4, 2],
              [4, 6, 2], [0, 5, 3], [5, 6, 4], [3, 2, 2]], 0, 6],
         [7, [[0, 1, 1], [1, 2, 2], [2, 6, 1],
              [0, 3, 4], [3, 6, 4], [0, 4, 2],
              [4, 6, 2], [0, 5, 3], [5, 6, 4]], 0, 6],
         [7, [[0, 1, 1], [1, 2, 1], [2, 6, 1],
              [0, 3, 1], [3, 6, 4], [0, 4, 2],
              [4, 6, 2], [0, 5, 3], [5, 6, 4]], 0, 6],
         [3, [[0, 1, 1], [1, 2, 1]], 0, 2]]
for t in tests:
    print(f"{t} -> {Solution().alternativeShortestPath(*t)}")

"""[7, [[0, 1, 1], [1, 2, 2], [2, 6, 1], [0, 3, 1], [3, 6, 4],
[0, 4, 2], [4, 6, 2], [0, 5, 3], [5, 6, 4]], 0, 6] -> 5
[7, [[0, 1, 1], [1, 2, 2], [2, 6, 1], [0, 3, 1], [3, 6, 4],
[0, 4, 2], [4, 6, 2], [0, 5, 3], [5, 6, 4], [3, 2, 2]], 0, 6] -> 7
[7, [[0, 1, 1], [1, 2, 2], [2, 6, 1], [0, 3, 4], [3, 6, 4],
[0, 4, 2], [4, 6, 2], [0, 5, 3], [5, 6, 4]], 0, 6] -> 7
[7, [[0, 1, 1], [1, 2, 1], [2, 6, 1], [0, 3, 1], [3, 6, 4],
[0, 4, 2], [4, 6, 2], [0, 5, 3], [5, 6, 4]], 0, 6] -> 4
[3, [[0, 1, 1], [1, 2, 1]], 0, 2] -> -1"""
