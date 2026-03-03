class Solution:
    def addingnIntegers(self, n: int, A: List[int]) -> int:
        from heapq import heapify, heappush, heappop
        heapify(A)
        cost = 0
        while len(A) > 1:
            s = heappop(A) + heappop(A)
            cost += s
            heappush(A, s)
        return cost


tests = [[3, [1, 2, 4]],
         [2, [7, 3]],
         [8, [1, 1, 1, 1, 1, 1, 1, 1]],
         [5, [32, 256, 128, 64, 32]],
         [5, [5, 1, 3, 2, 5]]]
for t in tests:
    print(f"{t} -> {Solution().addingnIntegers(*t)}")
'''
[3, [1, 2, 4]] -> 10
[2, [7, 3]] -> 10
[8, [1, 1, 1, 1, 1, 1, 1, 1]] -> 24
[5, [32, 256, 128, 64, 32]] -> 960
[5, [5, 1, 3, 2, 5]] -> 35
'''
