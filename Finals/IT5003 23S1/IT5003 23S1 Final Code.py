from typing import List


class Solution:
    def marketingPromotion(self, receipts: List[List[int]]) -> int:
        from heapq import heappush, heappop
        mh, Mh, f, ans = [], [], {}, 0
        for d in receipts:
            for x in d:
                heappush(mh, x)
                heappush(Mh, -x)
                f[x] = f.get(x, 0) + 1
            while f.get(-Mh[0], 0) == 0:
                heappop(Mh)
            M = -heappop(Mh)
            f[M] -= 1
            while f.get(mh[0], 0) == 0:
                heappop(mh)
            m = heappop(mh)
            f[m] -= 1
            ans += M - m
        return ans

    def lakeCurrents(self, grid: List[List[int]],
                     r1: int, c1: int, r2: int, c2: int) -> int:
        from collections import deque
        r, c = len(grid), len(grid[0])
        q = deque([(r1, c1)])
        dist = [[100000] * c for _ in range(r)]
        dist[r1][c1] = 0
        dirs = [(-1, 0), (-1, 1), (0, 1), (1, 1),
                (1, 0), (1, -1), (0, -1), (-1, -1)]
        while q:
            x, y = q.popleft()
            for d, (dx, dy) in enumerate(dirs):
                nx, ny = x + dx, y + dy
                if 0 <= nx < r and 0 <= ny < c:
                    cost = grid[x][y] != d
                    if dist[x][y] + cost < dist[nx][ny]:
                        dist[nx][ny] = dist[x][y] + cost
                        if cost:
                            q.appendleft((nx, ny))
                        else:
                            q.append((nx, ny))
        return dist[r2][c2]


tests = [[[[1, 2, 3], [1, 1], [10, 5, 5, 1]]],
         [[[1, 2, 3], [1, 1], [10, 5, 5, 1], [], [2]]],
         [[[100, 7, 8, 70, 25, 50, 70], [120, 5, 99], []]],
         [[[5, 5, 5], [5, 5]]],
         [[[1, 1], [2, 2], [3, 3], [4, 4]]]]
for t in tests:
    print(f"{t} -> {Solution().marketingPromotion(*t)}")
"""[[[1, 2, 3], [1, 1], [10, 5, 5, 1]]] -> 12
[[[1, 2, 3], [1, 1], [10, 5, 5, 1], [], [2]]] -> 19
[[[100, 7, 8, 70, 25, 50, 70], [120, 5, 99], []]] -> 299
[[[5, 5, 5], [5, 5]]] -> 0
[[[1, 1], [2, 2], [3, 3], [4, 4]]] -> 0"""

tests = [[[[0, 4, 1, 2, 5],
           [0, 3, 3, 5, 5],
           [6, 4, 7, 3, 4],
           [7, 2, 3, 7, 7],
           [0, 2, 0, 6, 2]], 4, 2, 2, 3],
         [[[0, 4, 1, 2, 5],
           [0, 3, 3, 5, 5],
           [6, 4, 7, 3, 4],
           [7, 2, 3, 7, 7],
           [0, 2, 0, 6, 2]], 3, 4, 0, 3],
         [[[0, 4, 1, 2, 5],
           [0, 3, 3, 5, 5],
           [6, 4, 7, 3, 4],
           [7, 2, 3, 7, 7],
           [0, 2, 0, 6, 2]], 0, 4, 1, 1],
         [[[0, 4, 1, 2, 5],
           [0, 3, 3, 5, 5],
           [6, 4, 7, 3, 4],
           [7, 2, 3, 7, 7],
           [0, 2, 0, 6, 2]], 0, 0, 4, 4]]
for t in tests:
    print(f"{t} -> {Solution().lakeCurrents(*t)}")
"""[[[0, 4, 1, 2, 5], [0, 3, 3, 5, 5], [6, 4, 7, 3, 4],
[7, 2, 3, 7, 7], [0, 2, 0, 6, 2]], 4, 2, 2, 3] -> 1
[[[0, 4, 1, 2, 5], [0, 3, 3, 5, 5], [6, 4, 7, 3, 4],
[7, 2, 3, 7, 7], [0, 2, 0, 6, 2]], 3, 4, 0, 3] -> 2
[[[0, 4, 1, 2, 5], [0, 3, 3, 5, 5], [6, 4, 7, 3, 4],
[7, 2, 3, 7, 7], [0, 2, 0, 6, 2]], 0, 4, 1, 1] -> 0
[[[0, 4, 1, 2, 5], [0, 3, 3, 5, 5], [6, 4, 7, 3, 4],
[7, 2, 3, 7, 7], [0, 2, 0, 6, 2]], 0, 0, 4, 4] -> 3"""
