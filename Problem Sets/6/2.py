# Matric Number: A0332008U
# Name: Li Jiaru
# Lab Group Number: B3B
# Lab TA Name: Manish Choudhary

from heapq import heappush, heappop
a, f = map(int, input().split())
g = [[] for _ in range(a)]
t = [[100000, 100000] for _ in range(a)]
t[0][0] = 0
p = [(0, 0, 0)]
for _ in range(f):
    o, d, c, m = input().split()
    g[int(o)].append((int(d), int(c), m == "A380"))
while p:
    i, o, u = heappop(p)
    if i != t[o][u]:
        continue
    for d, c, m in g[o]:
        nu = u or m
        ni = i + c
        if ni < t[d][nu]:
            t[d][nu] = ni
            heappush(p, (ni, d, nu))
print(-1 if t[a - 1][1] == 100000 else t[a - 1][1])
