from typing import List, Optional, Tuple


# Definition for a BSTvertex.
class BSTVertex:
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


class Solution:
    def deletingCharacters(self, s: str) -> str:
        stack = []
        for i in s:
            if i.isdigit():
                stack.pop()
            else:
                stack.append(i)
        return "".join(stack)

    def strengthCompetition(self, s: List[int]) -> int:
        from heapq import heapify, heappush, heappop
        s = [-i for i in s]
        heapify(s)
        while s:
            a = heappop(s)
            if not s:
                return -a
            b = heappop(s)
            if a != b:
                heappush(s, -abs(a - b))
        else:
            return 0

    def countingTriples(self, L: List[int], d: int) -> int:
        s = set(L)
        return sum(1 for i in L if i - d in s and i + d in s)

    def combiningIntegers(self, root1: Optional[BSTVertex],
                          root2: Optional[BSTVertex]) -> List[int]:
        def inorder(root: Optional[BSTVertex], result: List[int]) -> None:
            if not root:
                return
            inorder(root.left, result)
            result.append(root.value)
            inorder(root.right, result)

        a, b = [], []
        inorder(root1, a)
        inorder(root2, b)
        i = j = 0
        ans = []
        while i < len(a) and j < len(b):
            if a[i] <= b[j]:
                ans.append(a[i])
                i += 1
            else:
                ans.append(b[j])
                j += 1
        while i < len(a):
            ans.append(a[i])
            i += 1
        while j < len(b):
            ans.append(b[j])
            j += 1
        return ans

    # Alternative version
    def combiningIntegers_alt(self, root1: Optional[BSTVertex],
                              root2: Optional[BSTVertex]) -> List[int]:
        def push_left(node, stack):
            while node:
                stack.append(node)
                node = node.left
        s1, s2 = [], []
        push_left(root1, s1)
        push_left(root2, s2)
        ans = []
        while s1 or s2:
            if not s2 or (s1 and s1[-1].value <= s2[-1].value):
                node = s1.pop()
                push_left(node.right, s1)
            else:
                node = s2.pop()
                push_left(node.right, s2)
            ans.append(node.value)
        return ans

    def pairs(self, f: List[List[int]]) -> int:
        n = len(f)
        d = [sum(f[i]) for i in range(n)]
        return max(d[i] + d[j] - f[i][j] for i in range(n) for j in range(i + 1, n))

    # 14 mark version (Dijkstra, O(n^3 log n))
    def city_14(self, E: List[Tuple[int, int, int]], n: int, k: int) -> int:
        from collections import defaultdict
        from heapq import heappush, heappop
        g = defaultdict(list)
        for u, v, w in E:
            g[u].append((v, w))
            g[v].append((u, w))

        def dijkstra(i):
            dist = [float('inf')] * n
            dist[i] = 0
            q = [(0, i)]
            while q:
                d, u = heappop(q)
                if d > dist[u] or d > k:
                    continue
                for v, w in g[u]:
                    nd = d + w
                    if nd < dist[v] and nd <= k:
                        dist[v] = nd
                        heappush(q, (nd, v))
            return dist

        ans, best = -1, -1
        for i in range(n):
            d = dijkstra(i)
            c = sum(i != j and d[j] <= k for j in range(n))
            if c >= best:
                ans, best = i, c
        return ans

    # 15 mark version (Floyd-Warshall, O(n^3))
    def city_15(self, E: List[Tuple[int, int, int]], n: int, k: int) -> int:
        from math import inf
        d = [[inf] * n for _ in range(n)]
        for i in range(n):
            d[i][i] = 0
        for u, v, w in E:
            d[u][v] = d[v][u] = min(d[u][v], w)
        for x in range(n):
            for i in range(n):
                for j in range(n):
                    d[i][j] = min(d[i][j], d[i][x] + d[x][j])
        ans, best = -1, -1
        for i in range(n):
            c = sum(i != j and d[i][j] <= k for j in range(n))
            if c >= best:
                ans, best = i, c
        return ans


tests = ["xyz", "steven7halim", "abc12c", "th3qu1ckbr0wnf0xjumps0v3rth3l4zyd0g"]
for t in tests:
    print(f"{t} -> {Solution().deletingCharacters(t)}")
"""xyz -> xyz
steven7halim -> stevehalim
abc12c -> ac
th3qu1ckbr0wnf0xjumps0v3rth3l4zyd0g -> tqckbwnxjumprtzyg"""

tests = [[7, 7], [1, 5, 2], [2, 7, 4, 1, 15, 1], [99, 70, 96, 60]]
for t in tests:
    print(f"{t} -> {Solution().strengthCompetition(t)}")
"""[7, 7] -> 0
[1, 5, 2] -> 2
[2, 7, 4, 1, 15, 1] -> 0
[99, 70, 96, 60] -> 7"""

tests = [[[1, 2, 4, 5, 7, 10], 3], [[1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 3],
         [[1, 2, 3, 4, 5, 77, 79, 81], 2]]
for t in tests:
    print(f"{t} -> {Solution().countingTriples(*t)}")
"""[[1, 2, 4, 5, 7, 10], 3] -> 2
[[1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 3] -> 4
[[1, 2, 3, 4, 5, 77, 79, 81], 2] -> 2"""

root1 = BSTVertex(53)
root1.left = BSTVertex(3)
root1.left.right = BSTVertex(52)
root1.left.right.left = BSTVertex(27)
root2 = BSTVertex(81)
root2.left = BSTVertex(27)
root2.left.right = BSTVertex(39)
root2.right = BSTVertex(89)
print(Solution().combiningIntegers(root1, root2))
print(Solution().combiningIntegers_alt(root1, root2))
"""[3, 27, 27, 39, 52, 53, 81, 89]"""

tests = [[[0, 1, 0, 1, 0, 0, 0],
          [1, 0, 1, 1, 0, 0, 0],
          [0, 1, 0, 1, 1, 1, 0],
          [1, 1, 1, 0, 0, 0, 1],
          [0, 0, 1, 0, 0, 0, 0],
          [0, 0, 1, 0, 0, 0, 0],
          [0, 0, 0, 1, 0, 0, 0]]]
for t in tests:
    print(f"{t} -> {Solution().pairs(t)}")
"""[[0, 1, 0, 1, 0, 0, 0], [1, 0, 1, 1, 0, 0, 0], [0, 1, 0, 1, 1, 1, 0],
    [1, 1, 1, 0, 0, 0, 1], [0, 0, 1, 0, 0, 0, 0], [0, 0, 1, 0, 0, 0, 0],
    [0, 0, 0, 1, 0, 0, 0]] -> 7"""

tests = [[[(0, 4, 8), (0, 1, 2), (1, 4, 2), (1, 2, 3),
           (4, 2, 7), (4, 3, 1), (2, 3, 1)], 5, 2],
         [[(0, 1, 2), (2, 3, 2)], 4, 2],
         [[(0, 1, 1), (0, 2, 1), (1, 2, 1)], 3, 1],
         [[(0, 1, 1), (1, 2, 1), (2, 3, 1)], 4, 2]]
for t in tests:
    print(f"{t} -> {Solution().city_14(*t)}")
    print(f"{t} -> {Solution().city_15(*t)}")
"""[[(0, 4, 8), (0, 1, 2), (1, 4, 2), (1, 2, 3),
     (4, 2, 7), (4, 3, 1), (2, 3, 1)], 5, 2] -> 4
[[(0, 1, 2), (2, 3, 2)], 4, 2] -> 3
[[(0, 1, 1), (0, 2, 1), (1, 2, 1)], 3, 1] -> 2
[[(0, 1, 1), (1, 2, 1), (2, 3, 1)], 4, 2] -> 2"""
