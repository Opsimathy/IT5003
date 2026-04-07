# Matric Number: A0332008U
# Name: Li Jiaru
# Lab Group Number: B3B
# Lab TA Name: Manish Choudhary

from collections import deque

for _ in range(int(input())):
    p, n, l = input(), int(input()), input()[1:-1]
    if p.count("D") > n:
        print("error")
        continue
    l, r = deque(l.split(",")), False
    for i in p:
        if i == "R":
            r = not r
        else:
            l.pop() if r else l.popleft()
    print("[" + (",".join(reversed(l)) if r else ",".join(l)) + "]")
