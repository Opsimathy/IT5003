# Matric Number: A0332008U
# Name: Li Jiaru
# Lab Group Number: B3B
# Lab TA Name: Manish Choudhary

n, m, p = list(map(int, input().split()))
C = list(map(int, input().split()))
D = list(map(int, input().split()))
g = sorted([(c, d) for c in C for d in D],
           key=lambda x: x[0] / x[1], reverse=True)
f = True
for (c1, d1), (c2, d2) in zip(g, g[1:]):
    if 100 * c1 * d2 > (100 + p) * d1 * c2:
        print("Time to change gears!")
        f = False
        break
if f:
    print("Ride on!")
