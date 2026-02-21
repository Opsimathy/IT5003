class Solution:
    from typing import List

    def threeBagsofCandies(self, a: int, b: int, c: int) -> int:
        return 7 * min((a + b + c) // 2, a + b + c - max(a, b, c))


tests = [[1, 3, 4], [1, 2, 4], [7, 7, 1], [7, 5, 1], [2, 3, 5], [2, 2, 2]]
for t in tests:
    print(f"{t} -> {Solution().threeBagsofCandies(*t)}")
