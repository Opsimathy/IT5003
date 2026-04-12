class Solution:
    def ICPCProblem(self, s: str) -> bool:
        if len(s) % 4:
            return False
        stack = []
        for i in s:
            stack.append(i)
            if len(stack) >= 4 and stack[-4:] == ['i', 'c', 'p', 'c']:
                stack.pop()
                stack.pop()
                stack.pop()
                stack.pop()
        return not len(stack)

    def specialList(self, L: List[int]) -> List[int]:
        f = [0] * 101
        for i in L:
            f[i] += 1
        a = []
        if f[1] == 1 and f[2] == 0:
            a.append(1)
        for i in range(2, 100):
            if f[i] == 1 and f[i - 1] == f[i + 1] == 0:
                a.append(i)
        if f[100] == 1 and f[99] == 0:
            a.append(100)
        return a

    # Definition for a BSTvertex.
    class BSTVertex:
        def __init__(self, value=0, left=None, right=None):
            self.value = value
            self.left = left
            self.right = right

    def countVertices(self, root: Optional[BSTVertex]) -> int:
        def traverse(root):
            if root == None:
                return
            if root.value % 7 == 0:
                if root.left != None:
                    self.ans += 0 if root.left.right == None else 1
                    self.ans += 0 if root.left.left == None else 1
                if root.right != None:
                    self.ans += 1 if root.right.left != None else 0
                    self.ans += 1 if root.right.right != None else 0
            traverse(root.right)
            traverse(root.left)
        self.ans = 0
        traverse(root)
        return self.ans  # Overall time complexity is O(n)

    def orderinginaPhoto(self, pair: List[List[str]]) -> List[str]:
        from collections import defaultdict
        g = defaultdict(list)
        for i, j in pair:
            g[i].append(j)
            g[j].append(i)
        if len(pair) != len(g) - 1:
            return ["??"]
        ends = [i for i in g if len(g[i]) == 1]
        if len(ends) != 2 or any(len(g[i]) > 2 for i in g):
            return ["??"]
        ans = []
        prev, cur = None, min(ends)
        while cur is not None:
            ans.append(cur)
            nxt = [i for i in g[cur] if i != prev]
            prev, cur = cur, (nxt[0] if nxt else None)
        return ans if len(ans) == len(g) else ["??"]

    def shortestSwimRoute(self, grid: List[List[int]]) -> int:
        from collections import deque
        m, n = len(grid), len(grid[0])
        q = deque()
        dir = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        def dfs(i: int, j: int) -> None:
            if i < 0 or i >= m or j < 0 or j >= n or grid[i][j] != 1:
                return
            grid[i][j] = 2
            is_boundary = False
            for di, dj in dir:
                ni, nj = i + di, j + dj
                if 0 <= ni < m and 0 <= nj < n:
                    if grid[ni][nj] == 0:
                        is_boundary = True
                    elif grid[ni][nj] == 1:
                        dfs(ni, nj)
            if is_boundary:
                q.append((i, j))

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    dfs(i, j)
                    break
            else:
                continue
            break
        a = 0
        print(q)
        while q:
            for _ in range(len(q)):
                i, j = q.popleft()
                for di, dj in dir:
                    ni, nj = i + di, j + dj
                    if 0 <= ni < m and 0 <= nj < n:
                        if grid[ni][nj] == 1:
                            return a
                        elif grid[ni][nj] == 0:
                            grid[ni][nj] = 2
                            q.append((ni, nj))
            a += 1


tests = ["icicpcpc", "icpicpcc", "icpicpccicpc", "icpccpic", "icicicic", "icpci"]
for t in tests:
    print(f"{t} -> {Solution().ICPCProblem(t)}")
"""icicpcpc -> True
icpicpcc -> True
icpicpccicpc -> True
icpccpic -> False
icicicic -> False
icpci -> False"""

tests = [[3, 7, 1, 12, 5, 10, 8], [3, 7, 1, 12, 5, 10, 8, 3, 10],
         [3, 7, 1, 12, 5, 10, 8, 3, 10, 6]]
for t in tests:
    print(f"{t} -> {Solution().specialList(t)}")
"""[3, 7, 1, 12, 5, 10, 8] -> [1, 3, 5, 10, 12]
[3, 7, 1, 12, 5, 10, 8, 3, 10] -> [1, 5, 12]
[3, 7, 1, 12, 5, 10, 8, 3, 10, 6] -> [1, 12]"""

root = BSTVertex(53)
root.left = BSTVertex(17)
root.right = BSTVertex(77)
root.left.left = BSTVertex(12)
root.left.right = BSTVertex(50)
root.left.left.left = BSTVertex(3)
root.left.left.right = BSTVertex(14)
root.left.left.left.left = BSTVertex(1)
root.left.right.left = BSTVertex(31)
root.left.right.left.right = BSTVertex(35)
root.left.right.left.right.right = BSTVertex(38)
root.right.left = BSTVertex(74)
root.right.right = BSTVertex(83)
root.right.left.right = BSTVertex(75)
root.right.right.left = BSTVertex(80)
root.right.right.right = BSTVertex(98)
root.right.right.right.left = BSTVertex(90)
root.right.right.right.right = BSTVertex(99)
root.right.right.right.left.right = BSTVertex(95)
print(Solution().countVertices(root))
"""4"""

tests = [[["steven", "grace"], ["arief", "erlyn"], ["arief", "steven"]],
         [["steven", "grace"]],
         [["steven", "grace"], ["arief", "grace"], ["arief", "steven"]],
         [["steven", "grace"], ["arief", "steven"], ["steven", "erlyn"]],
         [["steven", "grace"], ["arief", "erlyn"]]]
for t in tests:
    print(f"{t} -> {Solution().orderinginaPhoto(t)}")
"""[['steven', 'grace'], ['arief', 'erlyn'], ['arief', 'steven']]
-> ['erlyn', 'arief', 'steven', 'grace']
[['steven', 'grace']] -> ['grace', 'steven']
[['steven', 'grace'], ['arief', 'grace'], ['arief', 'steven']] -> ['??']
[['steven', 'grace'], ['arief', 'steven'], ['steven', 'erlyn']] -> ['??']
[['steven', 'grace'], ['arief', 'erlyn']] -> ['??']"""

tests = [[[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
          [0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 1, 1, 0, 0],
          [1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 1],
          [1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1],
          [1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1],
          [0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]],
         [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
          [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0]]]
for t in tests:
    print(f"{t} -> {Solution().shortestSwimRoute(t)}")
"""[[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 1, 1, 0, 0],
    [1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 1],
    [1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1],
    [1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1],
    [0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]] -> 5
[[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
 [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0]] -> 7"""
