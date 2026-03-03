class Solution:
    from typing import List

    def gridProblem(self, grid: List[List[int]], limits: List[int], k: int) -> int:
        def select(a, k):  # returns the kth smallest element using median-of-medians, O(n)
            while True:
                n = len(a)
                if n <= 25:
                    return sorted(a)[k]
                m = [sorted(a[i:i + 5])[len(a[i:i + 5]) // 2] for i in range(0, n, 5)]
                p = select(m, len(m) // 2)
                l, h = [_ for _ in a if _ < p], [_ for _ in a if _ > p]
                if k < len(l):
                    a = l
                elif k < n - len(h):
                    return p
                else:
                    k -= n - len(h)
                    a = h
        a = []
        for i, r in enumerate(grid):
            t = limits[i]
            if t == 0:
                continue
            c = select(r, len(r) - t)
            l = [x for x in r if x > c]
            a += l
            if t - len(l) > 0:
                a += [c] * (t - len(l))
        if k >= len(a):
            return sum(a)
        c = select(a, len(a) - k)
        l = [x for x in a if x > c]
        return sum(l) + c * (k - len(l))


tests = [[[[7, 7, 7], [7, 7, 7]], [1, 3], 2],
         [[[5, 10, 3, 1]], [3], 2],
         [[[1, 2, 3], [4, 5, 6], [7, 8, 9]], [3, 2, 1], 2],
         [[[22, 1, 33], [21, 4, 77]], [2, 3], 3]]
for t in tests:
    print(f"{t} -> {Solution().gridProblem(*t)}")
