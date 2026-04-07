# Matric Number: A0332008U
# Name: Li Jiaru
# Lab Group Number: B3B
# Lab TA Name: Manish Choudhary

n, k = list(map(int, input().split()))
a = input().split()
p, i = [0], 0
while i < len(a):
    if a[i] == "undo":
        p = p[:-int(a[i + 1])]
        i += 2
    else:
        p.append((p[-1] + int(a[i])) % n)
        i += 1
print(p[-1])
