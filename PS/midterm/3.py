# Matric Number: A0332008U
# Name: Li Jiaru
# Lab Group Number: B3B
# Lab TA Name: Manish Choudhary

def count(a):
    if len(a) <= 1:
        return 0, a
    c1, l = count(a[:len(a) // 2])
    c2, r = count(a[len(a) // 2:])
    c = c1 + c2
    m = []
    i = j = 0
    while i < len(l) and j < len(r):
        if l[i] <= r[j]:
            m.append(l[i])
            i += 1
        else:
            m.append(r[j])
            c += len(l) - i
            j += 1
    return c, m + l[i:] + r[j:]


n = [int(input()) for _ in range(int(input()))]
print(count(n)[0])
