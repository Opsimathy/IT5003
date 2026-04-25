from typing import List, Tuple, Set


class Solution:
    # A.1 Archery Practice
    def archery(self, shots: List[Tuple[int, int]], k: int) -> int:
        from heapq import heappush, heappop
        h = []
        ans = 0
        for x, y in shots:
            d = abs(x) + abs(y)
            heappush(h, -d)
            if len(h) > k:
                heappop(h)
            if len(h) == k:
                ans += -h[0]
        return ans

    # A.2 Integer Sibling Groups
    def countSiblingGroups(self, S: Set[int]) -> int:
        digit_sums = set()
        for x in S:
            digit_sums.add(self.get_digit_sum(x))
        return len(digit_sums)

    def get_digit_sum(self, n: int) -> int:
        total = 0
        while n > 0:
            total += n % 10
            n //= 10
        return total

    # A.4 Strongest Trinity
    def maxTrinityStrength(self, n: int, EL: List[Tuple[int, int]]) -> int:
        adj = [set() for _ in range(n + 1)]
        for u, v in EL:
            adj[u].add(v)
            adj[v].add(u)
        deg = [len(adj[i]) for i in range(n + 1)]
        return max((deg[u] + deg[v] + deg[w] - 6 for u, v in EL
                    for w in adj[u] & adj[v]), default=-1)

    # A.5 Yoshi's Tasks
    def yoshiTasks(self, n: int, edges: List[Tuple[int, int]]) -> List[int]:
        from heapq import heapify, heappush, heappop
        g = [[] for _ in range(n + 1)]
        d = [0] * (n + 1)
        for u, v in edges:
            g[u].append(v)
            d[v] += 1
        h = [i for i in range(1, n + 1) if d[i] == 0]
        heapify(h)
        ans = []
        while h:
            u = heappop(h)
            ans.append(u)
            for v in g[u]:
                d[v] -= 1
                if d[v] == 0:
                    heappush(h, v)
        return ans if len(ans) == n else [-1]

    # A.6 The Last Question
    def theLastQuestion(self, n: int,
                        edges: List[Tuple[int, int, int]]) -> int:
        from heapq import heappush, heappop
        from math import inf

        def dijkstra(s):
            g = [[] for _ in range(n)]
            for u, v, w in edges:
                g[u].append((v, w))
                g[v].append((u, w))
            dist = [inf] * n
            dist[s] = 0
            q = [(0, s)]
            while q:
                d, u = heappop(q)
                if d != dist[u]:
                    continue
                for v, w in g[u]:
                    if d + w < dist[v]:
                        dist[v] = d + w
                        heappush(q, (dist[v], v))
            return dist
        d1 = dijkstra(0)
        d2 = dijkstra(n - 1)
        d = d1[n - 1]
        return sum(d1[u] + w + d2[v] == d or d1[v] + w + d2[u] == d
                   for u, v, w in edges)


tests = [[[(1, 1), (3, 4), (2, 1), (-1, 0)], 2], [[(1, 0), (0, 1), (2, 0)], 2]]
for t in tests:
    print(f"{t} -> {Solution().archery(*t)}")
"""[[(1, 1), (3, 4), (2, 1), (-1, 0)], 2] -> 12
[[(1, 0), (0, 1), (2, 0)], 2] -> 2"""

tests = [{5, 6, 7, 23, 24, 33, 51, 123}, {12, 21, 30, 5}, {10, 20, 11, 101, 99}]
for t in tests:
    print(f"{t} -> {Solution().countSiblingGroups(t)}")
"""{33, 5, 6, 7, 51, 23, 24, 123} -> 3
{5, 12, 21, 30} -> 2
{99, 20, 101, 10, 11} -> 3"""

tests = [[7, [(1, 2), (1, 3), (2, 3), (1, 4), (2, 5), (3, 6), (6, 7)]],
         [7, [(1, 2), (1, 3), (1, 4), (2, 5), (3, 6), (6, 7)]],
         [6, [(1, 2), (1, 3), (2, 3), (1, 4), (2, 5), (3, 6)]],
         [5, [(1, 2), (2, 3), (1, 3), (1, 4), (2, 4), (3, 4)]]]
for t in tests:
    print(f"{t} -> {Solution().maxTrinityStrength(*t)}")
"""[7, [(1, 2), (1, 3), (2, 3), (1, 4), (2, 5), (3, 6), (6, 7)]] -> 3
[7, [(1, 2), (1, 3), (1, 4), (2, 5), (3, 6), (6, 7)]] -> -1
[6, [(1, 2), (1, 3), (2, 3), (1, 4), (2, 5), (3, 6)]] -> 3
[5, [(1, 2), (2, 3), (1, 3), (1, 4), (2, 4), (3, 4)]] -> 3"""

tests = [[5, [(1, 4), (4, 2), (1, 2), (1, 5)]],
         [5, [(1, 4), (4, 2), (2, 1), (1, 5)]]]
for t in tests:
    print(f"{t} -> {Solution().yoshiTasks(*t)}")
"""[5, [(1, 4), (4, 2), (1, 2), (1, 5)]] -> [1, 3, 4, 2, 5]
[5, [(1, 4), (4, 2), (2, 1), (1, 5)]] -> [-1]"""

tests = [[6, [(0, 1, 1), (0, 2, 1), (0, 3, 4), (1, 4, 3),
              (2, 3, 2), (3, 4, 1), (4, 5, 3)]]]
for t in tests:
    print(f"{t} -> {Solution().theLastQuestion(*t)}")
"""[6, [(0, 1, 1), (0, 2, 1), (0, 3, 4), (1, 4, 3),
        (2, 3, 2), (3, 4, 1), (4, 5, 3)]] -> 6"""
