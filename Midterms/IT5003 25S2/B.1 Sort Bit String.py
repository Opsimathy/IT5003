class Solution:
    def sortBitString(self, s: str) -> int:
        l = map(int, list(s[::-1]))
        ans = i = j = 0
        for c in l:
            if c:
                ans += i - j
                j += 1
            i += 1
        return ans


tests = ["10", "1010", "0000011110100000110101101010"]
for t in tests:
    print(f"{t} -> {Solution().sortBitString(t)}")
'''10 -> 1
1010 -> 3
0000011110100000110101101010 -> 77'''
