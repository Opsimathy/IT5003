# Matric Number: A0332008U
# Name: Li Jiaru
# Lab Group Number: B3B
# Lab TA Name: Manish Choudhary

n, m = map(int, input().split())
e = {}
for i in range(1, m + 1):
    a, b = map(int, input().split())
    if a > b:
        a, b = b, a
    e[(a, b)] = i
a = []
for i in range(1, n + 1):
    t = (i, i + 1) if i < n else (1, n)
    if t not in e:
        print("impossible")
        break
    a.append(e[t])
else:
    print(*a, sep='\n')
