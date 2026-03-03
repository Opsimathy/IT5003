class Solution:
    def specialLargestGap(self, arr: List[int]) -> int:
        def sod(n: int) -> int:
            s = 0
            while n:
                s += n % 10
                n //= 10
            return s
        m = [float('inf')] * 64
        M = [-1] * 64
        c = [0] * 64
        for i in arr:
            s = sod(i)
            m[s] = min(m[s], i)
            M[s] = max(M[s], i)
            c[s] += 1
        a = -1
        for s in range(64):
            if c[s] >= 2:
                a = max(a, M[s] - m[s])
        return a


tests = [[[63, 123, 27, 77, 7, 239, 45]],
         [[7, 16, 25, 34, 43, 52, 61, 70]],
         [[10, 2, 77, 14]]]
for t in tests:
    print(f"{t} -> {Solution().specialLargestGap(*t)}")
'''
[[63, 123, 27, 77, 7, 239, 45]] -> 162
[[7, 16, 25, 34, 43, 52, 61, 70]] -> 63
[[10, 2, 77, 14]] -> -1
'''
