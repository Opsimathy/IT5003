# Matric Number: A0332008U
# Name: Li Jiaru
# Lab Group Number: B3B
# Lab TA Name: Manish Choudhary

n = int(input())
s, a, b, c = [input() for _ in range(n)], [-1] * n, [-1] * n, list(range(n))
for _ in range(n - 1):
    i, j = map(int, input().split())
    a[c[i - 1]] = j - 1
    c[i - 1] = c[j - 1]
    b[j - 1] = 1
m, l = b.index(-1), []
while m != -1:
    l.append(s[m])
    m = a[m]
print("".join(l))
