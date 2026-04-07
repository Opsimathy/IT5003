# Matric Number: A0332008U
# Name: Li Jiaru
# Lab Group Number: B3B
# Lab TA Name: Manish Choudhary

from heapq import heappush, heappop
a = sorted((s, t) for t, s in (map(int, input().split()) for _ in range(int(input()))))
o = d = 0
h = []
for s, t in a:
    o += t
    heappush(h, -t)
    while o > s:
        c = -heappop(h)
        heappush(h, -(c // 2))
        o -= c - c // 2
        d += 1
print(d)
