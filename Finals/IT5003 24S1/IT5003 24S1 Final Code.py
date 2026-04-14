from typing import List, Optional, Tuple


# Definition for a BSTvertex.
class BSTVertex:
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def printBST(root, level=0):
    if root is not None:
        printBST(root.right, level + 1)
        print('    ' * level + str(root.value))
        printBST(root.left, level + 1)


class Solution:
    def buddySystem_naive(self, L: List[int]) -> int:
        s = 0
        for i in range(len(L)):
            for j in range(i - 1, -1, -1):
                if L[j] < L[i]:
                    s += L[j]
                    break
        return s

    def buddySystem(self, L: List[int]) -> int:
        s = 0
        stack = []
        for h in L:
            while stack and stack[-1] >= h:
                stack.pop()
            if stack:
                s += stack[-1]
            stack.append(h)
        return s

    def BSTMerging_naive(self, A: Optional[BSTVertex],
                         B: Optional[BSTVertex]) -> Optional[BSTVertex]:
        def inorder(root, arr):
            if not root:
                return
            inorder(root.left, arr)
            arr.append(root.value)
            inorder(root.right, arr)
        arrA, arrB = [], []
        inorder(A, arrA)
        inorder(B, arrB)

        def build(arr):
            if not arr:
                return None
            mid = len(arr) // 2
            root = BSTVertex(arr[mid])
            root.left = build(arr[:mid])
            root.right = build(arr[mid + 1:])
            return root
        return build(arrA + arrB)

    def BSTMerging(self, A: Optional[BSTVertex],
                   B: Optional[BSTVertex]) -> Optional[BSTVertex]:
        if not A:
            return B
        if not B:
            return A
        currA = A
        currB = B
        while currA.right and currB.left:
            currA = currA.right
            currB = currB.left
        if not currA.right:
            currA.right = B
            return A
        else:
            currB.left = A
            return B

    def bingeReading(self, n: int, m: int, pages: List[int],
                     deps: List[Tuple[int, int]]) -> int:
        g = [[] for _ in range(n)]
        o = [0] * n
        for u, v in deps:
            g[v - 1].append(u - 1)
            o[u - 1] += 1
        S = [i for i in range(n) if o[i] == 0]
        need = []
        for s in S:
            v = [0] * n
            stack = [s]
            v[s] = 1
            while stack:
                u = stack.pop()
                for p in g[u]:
                    if not v[p]:
                        v[p] = 1
                        stack.append(p)
            need.append(v)
        return min(sum(pages[x] for x in range(n) if need[i][x] or need[j][x])
                   for i in range(len(S)) for j in range(i + 1, len(S)))

    # Alternative version via bitmask DP
    def bingeReading_alt(self, n: int, m: int, pages: List[int],
                         deps: List[Tuple[int, int]]) -> int:
        g = [[] for _ in range(n)]
        o = [0] * n
        for u, v in deps:
            g[u - 1].append(v - 1)
            o[u - 1] += 1
        need = [1 << i for i in range(n)]
        for u in range(n):
            for v in g[u]:
                need[v] |= need[u]
        S = [i for i in range(n) if o[i] == 0]
        ans = 10 ** 10
        for i in range(len(S)):
            for j in range(i + 1, len(S)):
                mask = need[S[i]] | need[S[j]]
                total = sum(pages[k] for k in range(n) if (mask >> k) & 1)
                ans = min(ans, total)
        return ans


tests = [[1, 2, 3, 4, 5, 6, 7], [8, 3, 9, 5, 2, 6, 9]]
for t in tests:
    print(f"{t} -> {Solution().buddySystem_naive(t)}")
    print(f"{t} -> {Solution().buddySystem(t)}")
"""[1, 2, 3, 4, 5, 6, 7] -> 21
[8, 3, 9, 5, 2, 6, 9] -> 14"""

root1 = BSTVertex(53)
root1.left = BSTVertex(3)
root1.left.right = BSTVertex(52)
root1.left.right.left = BSTVertex(27)
root2 = BSTVertex(81)
root2.left = BSTVertex(67)
root2.left.right = BSTVertex(69)
root2.right = BSTVertex(89)
printBST(root1)
print("\n")
printBST(root2)
print("\n")
printBST(Solution().BSTMerging_naive(root1, root2))
print("\n")
printBST(Solution().BSTMerging(root1, root2))
"""
53
        52
            27
    3


    89
81
        69
    67


        89
    81
        69
67
        53
    52
        27
            3


        89
    81
            69
        67
53
        52
            27
    3
"""

tests = [[4, 2, [10, 7, 5, 2], [(1, 3), (1, 4)]],
         [5, 2, [10, 7, 4, 6, 15], [(1, 4), (2, 3)]],
         [5, 0, [8, 3, 10, 2, 7], []]]
for t in tests:
    print(f"{t} -> {Solution().bingeReading(*t)}")
    print(f"{t} -> {Solution().bingeReading_alt(*t)}")
"""[4, 2, [10, 7, 5, 2], [(1, 3), (1, 4)]] -> 17
[5, 2, [10, 7, 4, 6, 15], [(1, 4), (2, 3)]] -> 26
[5, 0, [8, 3, 10, 2, 7], []] -> 5"""
