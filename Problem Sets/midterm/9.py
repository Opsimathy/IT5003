# Matric Number: A0332008U
# Name: Li Jiaru
# Lab Group Number: B3B
# Lab TA Name: Manish Choudhary

from collections import deque

n, m, c = list(map(int, input().split()))
a = list(map(int, input().split()))
mi, ma, l = deque(), deque(), []
for i, j in enumerate(a):
    while mi and a[mi[-1]] >= j:
        mi.pop()
    while ma and a[ma[-1]] <= j:
        ma.pop()
    mi.append(i)
    ma.append(i)
    s = i - m + 1
    if s >= 0:
        while mi[0] < s:
            mi.popleft()
        while ma[0] < s:
            ma.popleft()
        if a[ma[0]] - a[mi[0]] <= c:
            l.append(str(s + 1))
print("\n".join(l) if l else "NONE")
