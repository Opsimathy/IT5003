# Matric Number: A0332008U
# Name: Li Jiaru
# Lab Group Number: B3B
# Lab TA Name: Manish Choudhary

n = int(input())
a = list(map(int, input().split()))
p, s = [a[0]] + [0] * (n - 1), [0] * (n - 1) + [a[-1]]
for i in range(1, n):
    p[i] = max(p[i - 1], a[i])
    s[~i] = min(s[-i], a[~i])
c = 0
for i in range(n):
    if p[i] <= a[i] and a[i] <= s[i]:
        c += 1
print(c)
