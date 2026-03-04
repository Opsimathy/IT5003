class Solution:
    def minimumNumberofMoves(self, nums: List[int], t: int) -> int:
        from heapq import heapify, heappop, heappush
        heapify(nums)
        moves = 0
        while True:
            x = heappop(nums)
            if x >= t:
                return moves
            y = heappop(nums)
            heappush(nums, 4 * x + 2 * y)
            moves += 1


tests = [[[7, 1, 2, 3], 8]]
for t in tests:
    print(f"{t} -> {Solution().minimumNumberofMoves(*t)}")
"""[[7, 1, 2, 3], 8] -> 2"""
