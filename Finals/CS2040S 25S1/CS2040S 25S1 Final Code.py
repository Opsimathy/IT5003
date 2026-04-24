from typing import List, Optional, Tuple


# Definition for a BSTvertex.
class BSTVertex:
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


class Solution:
    def earliestTime(self, n: int, understood: List[int], solve: List[int]) -> int:
        return min(understood[i] + solve[i] for i in range(n))

    def fourthPower(self, A: List[int]) -> List[int]:
        ans = []
        l, r = 0, len(A) - 1
        while l <= r:
            if abs(A[l]) > abs(A[r]):
                ans.append(A[l] ** 4)
                l += 1
            else:
                ans.append(A[r] ** 4)
                r -= 1
        return ans

    def robotMovement(self, C: str) -> bool:
        x = y = 7
        seen = {(x, y)}
        for c in C:
            if c == 'U':
                y += 1
            elif c == 'R':
                x += 1
            elif c == 'D':
                y -= 1
            elif c == 'L':
                x -= 1
            if (x, y) in seen:
                return True
            seen.add((x, y))
        return False

    def specialBinaryTree(self, root: Optional[BSTVertex]) -> int:
        ans = 0

        def dfs(node: Optional[BSTVertex]):
            nonlocal ans
            if not node:
                return 0, 0
            lh, ls = dfs(node.left)
            rh, rs = dfs(node.right)
            if lh == rh and ls != -1 and rs != -1:
                size = ls + rs + 1
                ans = max(ans, size)
                return lh + 1, size
            return -1, -1
        dfs(root)
        return ans

    def superstar(self, n: int, edges: List[Tuple[int, int]],
                  value: List[int], k: int) -> int:
        from heapq import nlargest
        g = [[] for _ in range(n)]
        for u, v in edges:
            if value[v] > 0:
                g[u].append(value[v])
            if value[u] > 0:
                g[v].append(value[u])
        return max(value[i] + sum(nlargest(k, g[i]))
                   for i in range(n))

    def completingErrands(self, grid: List[List[int]]) -> float:
        from collections import deque
        from math import inf
        m, n = len(grid), len(grid[0])
        if not grid[0][0]:
            return inf
        special = sorted((grid[r][c], r, c) for r in range(m)
                         for c in range(n) if grid[r][c] > 1)

        def bfs(sr, sc, tr, tc):
            q = deque([(sr, sc, 0)])
            seen = {(sr, sc)}
            while q:
                r, c, d = q.popleft()
                if (r, c) == (tr, tc):
                    return d
                for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < m and 0 <= nc < n and grid[nr][nc]\
                       and (nr, nc) not in seen:
                        seen.add((nr, nc))
                        q.append((nr, nc, d + 1))
            return inf
        ans, r, c = 0, 0, 0
        for _, tr, tc in special:
            d = bfs(r, c, tr, tc)
            if d == inf:
                return d
            ans += d
            r, c = tr, tc
        return ans


tests = [[2, [4, 5], [5, 2]], [3, [8, 8, 8], [60, 20, 30]],
         [4, [15, 20, 18, 16], [20, 20, 20, 20]]]
for t in tests:
    print(f"{t} -> {Solution().earliestTime(*t)}")
"""[2, [4, 5], [5, 2]] -> 7
[3, [8, 8, 8], [60, 20, 30]] -> 28
[4, [15, 20, 18, 16], [20, 20, 20, 20]] -> 35"""

tests = [[-7, -7, 2, 9], [1, 2, 2, 4, 5], [-3, -2, -1]]
for t in tests:
    print(f"{t} -> {Solution().fourthPower(t)}")
"""[-7, -7, 2, 9] -> [6561, 2401, 2401, 16]
[1, 2, 2, 4, 5] -> [625, 256, 16, 16, 1]
[-3, -2, -1] -> [81, 16, 1]"""

tests = ["URDL", "URDLL", "UURR", "DUDUDUDU"]
for t in tests:
    print(f"{t} -> {Solution().robotMovement(t)}")
"""URDL -> True
URDLL -> True
UURR -> False
DUDUDUDU -> True"""


root = BSTVertex(13)
root.left = BSTVertex(12)
root.left.left = BSTVertex(2)
root.right = BSTVertex(47)
root.right.left = BSTVertex(21)
root.right.left.left = BSTVertex(18)
root.right.left.right = BSTVertex(32)
root.right.left.right.left = BSTVertex(30)
root.right.left.right.left.left = BSTVertex(26)
root.right.left.right.left.right = BSTVertex(31)
root.right.right = BSTVertex(57)
root.right.right.left = BSTVertex(54)
root.right.right.left.left = BSTVertex(52)
root.right.right.left.right = BSTVertex(55)
root.right.right.right = BSTVertex(66)
root.right.right.right.left = BSTVertex(62)
root.right.right.right.right = BSTVertex(79)
print(Solution().specialBinaryTree(root))
"""7"""

edges = [(0, 1), (1, 2), (1, 3), (2, 4), (3, 4), (3, 5), (3, 6)]
tests = [[7, edges, [1, 2, 3, 4, 70, -77, 2], 2],
         [7, edges, [1, 2, 3, 4, 70, -77, 2], 6],
         [7, edges, [1, 2, 3, 4, 70, -77, 2], 1],
         [7, edges, [1, 2, 3, 4, 70, -77, 2], 0]]
for t in tests:
    print(f"{t} -> {Solution().superstar(*t)}")
"""[7, ..., [1, 2, 3, 4, 70, -77, 2], 2] -> 77
[7, ..., [1, 2, 3, 4, 70, -77, 2], 6] -> 78
[7, ..., [1, 2, 3, 4, 70, -77, 2], 1] -> 74
[7, ..., [1, 2, 3, 4, 70, -77, 2], 0] -> 70"""

tests = [[[[1, 0, 0, 0, 0, 0],
           [2, 0, 5, 1, 6, 0],
           [3, 1, 4, 1, 7, 0],
           [1, 1, 1, 1, 1, 0],
           [1, 1, 1, 1, 1, 0],
           [0, 0, 0, 0, 0, 0]]],
         [[[1, 1, 1],
           [7, 0, 77],
           [1, 0, 1],
           [1, 1, 1]]],
         [[[1, 1, 1],
           [7, 0, 77],
           [99, 0, 1],
           [1, 1, 1]]],
         [[[1, 0, 1],
           [7, 0, 77],
           [1, 0, 1],
           [1, 0, 1]]]]
for t in tests:
    print(f"{t} -> {Solution().completingErrands(*t)}")
"""[[[1, 0, 0, 0, 0, 0], [2, 0, 5, 1, 6, 0], [3, 1, 4, 1, 7, 0],
     [1, 1, 1, 1, 1, 0], [1, 1, 1, 1, 1, 0], [0, 0, 0, 0, 0, 0]]] -> 8
[[[1, 1, 1], [7, 0, 77], [1, 0, 1], [1, 1, 1]]] -> 5
[[[1, 1, 1], [7, 0, 77], [99, 0, 1], [1, 1, 1]]] -> 10
[[[1, 0, 1], [7, 0, 77], [1, 0, 1], [1, 0, 1]]] -> inf"""
