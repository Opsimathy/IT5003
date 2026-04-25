from typing import List, Tuple, Optional, Set


class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


class UnionFind:
    def __init__(self, n: int):
        self.parent = list(range(n))
        self.rank = [0] * n
        self.num_sets = n

    def find(self, x: int) -> int:
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union_set(self, a: int, b: int) -> None:
        ra, rb = self.find(a), self.find(b)
        if ra == rb:
            return
        if self.rank[ra] < self.rank[rb]:
            ra, rb = rb, ra
        self.parent[rb] = ra
        if self.rank[ra] == self.rank[rb]:
            self.rank[ra] += 1
        self.num_sets -= 1

    def num_disjoint_sets(self) -> int:
        return self.num_sets


class Solution:
    # A.1 Archery Practice
    def archery(self, shots: List[Tuple[int, int]], k: int) -> int:
        from sortedcontainers import SortedList
        S = SortedList()
        ans = 0
        for x, y in shots:
            d = abs(x) + abs(y)
            S.add(d)
            if len(S) >= k:
                ans += sorted(S)[k - 1]
        return ans

    # A.2 Integer Sibling Groups
    def countSiblingGroups(self, S: Set[int]) -> int:
        nums = list(S)
        n = len(nums)
        if n == 0:
            return 0
        uf = UnionFind(n)
        digit_sums = [self.get_digit_sum(x) for x in nums]
        for i in range(n):
            for j in range(i + 1, n):
                if digit_sums[i] == digit_sums[j]:
                    uf.union_set(i, j)
        return uf.num_disjoint_sets()

    def get_digit_sum(self, n: int) -> int:
        total = 0
        while n > 0:
            total += n % 10
            n //= 10
        return total

    # A.3 VisuAlgo AVL Tree Visualization
    # SolutionTwin version
    def balanceBST_twin(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        nodes: List[int] = []
        self.inorder_twin(root, nodes)
        return self.build_twin(nodes, 0, len(nodes) - 1)

    def inorder_twin(self, root: Optional[TreeNode], nodes: List[int]) -> None:
        if not root:
            return
        self.inorder_twin(root.left, nodes)
        nodes.append(root.value)
        self.inorder_twin(root.right, nodes)

    def build_twin(self, nodes: List[int], l: int, r: int) -> Optional[TreeNode]:
        if l > r:
            return None
        m = (l + r) // 2
        node = TreeNode(nodes[m])
        node.left = self.build_twin(nodes, l, m - 1)
        node.right = self.build_twin(nodes, m + 1, r)
        return node

    # SolutionTalk version
    def __init__(self):
        self.a = []

    def balanceBST_talk(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # self.a = []
        self.inorder_talk(root)
        return self.build_talk(0, len(self.a) - 1)

    def inorder_talk(self, root: Optional[TreeNode]) -> None:
        if not root:
            return
        self.inorder_talk(root.left)
        self.a.append(root.value)
        self.inorder_talk(root.right)

    def build_talk(self, l: int, r: int) -> Optional[TreeNode]:
        if l > r:
            return None
        m = (l + r) >> 1
        node = TreeNode(self.a[m])
        node.left = self.build_talk(l, m - 1)
        node.right = self.build_talk(m + 1, r)
        return node

    # A.4 Strongest Trinity
    def maxTrinityStrength(self, n: int, EL: List[Tuple[int, int]]) -> int:
        AM = [[0] * (n + 1) for _ in range(n + 1)]
        for u, v in EL:
            AM[u][v] = AM[v][u] = 1
        ans = -1
        for i in range(1, n + 1):
            for j in range(i + 1, n + 1):
                for k in range(j + 1, n + 1):
                    if AM[i][j] and AM[j][k] and AM[i][k]:
                        strength = 0
                        for x in range(1, n + 1):
                            if x in (i, j, k):
                                continue
                            if AM[i][x]:
                                strength += 1
                            if AM[j][x]:
                                strength += 1
                            if AM[k][x]:
                                strength += 1
                        ans = max(ans, strength)
        return ans


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


def inorder(root):
    if not root:
        return []
    return inorder(root.left) + [root.value] + inorder(root.right)


def height(root):
    if not root:
        return -1
    return 1 + max(height(root.left), height(root.right))


root = TreeNode(37)
root.left = TreeNode(28)
root.left.left = TreeNode(24)
root.right = TreeNode(44)
root.right.right = TreeNode(83)
root.right.right.left = TreeNode(56)
root.right.right.left.left = TreeNode(46)
root.right.right.left.right = TreeNode(63)
root.right.right.right = TreeNode(93)
root.right.right.right.left = TreeNode(91)
b1 = Solution().balanceBST_twin(root)
b2 = Solution().balanceBST_talk(root)
print(f"{inorder(root), height(root)} -> {inorder(b1), height(b1)}")
print(f"{inorder(root), height(root)} -> {inorder(b2), height(b2)}")

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
