class Solution:
    def specialOperations(self, arr: List[int], m: int) -> int:
        from heapq import heapify, heappush, heappop
        n = len(arr)
        arr = list(map(lambda x: -x, arr))
        heapify(arr)
        total = 0
        for _ in range(min(m, 6 * n)):
            x = -heappop(arr)
            total += x
            heappush(arr, -max(x // 7, 7))
        return total + 7 * (m - 6 * n) if m > 6 * n else total


tests = [[[49, 49, 49], 4],
         [[441, 7, 8, 34], 4],
         [[441, 7, 8, 34], 77]]
for t in tests:
    print(f"{t} -> {Solution().specialOperations(*t)}")
'''
[[49, 49, 49], 4] -> 154
[[441, 7, 8, 34], 4] -> 547
[[441, 7, 8, 34], 77] -> 1059
'''
