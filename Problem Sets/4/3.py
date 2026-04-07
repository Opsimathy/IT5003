# Matric Number: A0332008U
# Name: Li Jiaru
# Lab Group Number: B3B
# Lab TA Name: Manish Choudhary

a = {}
for _ in range(int(input())):
    p = ""
    for i in input():
        p += i
        a[p] = a.get(p, 0) + 1
for _ in range(int(input())):
    print(a.get(input(), 0))
