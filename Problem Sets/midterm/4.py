# Matric Number: A0332008U
# Name: Li Jiaru
# Lab Group Number: B3B
# Lab TA Name: Manish Choudhary

n, t = list(map(int, input().split()))
a = list(map(int, input().split()))
if t == 1:  # two-sum, O(n)
    s, f = set(), False
    for i in a:
        if 7777 - i in s:
            f = True
            break
        s.add(i)
    print("Yes" if f else "No")
if t == 2:  # O(n)
    print("Unique" if len(a) == len(set(a)) else "Contains duplicate")
if t == 3:  # Boyer-Moore, O(n)
    m, c = -1, 0
    for i in a:
        if c == 0:
            m = i
        c += 1 if m == i else -1
    print(m if a.count(m) > len(a) // 2 else -1)
if t == 4:  # median-of-medians, O(n)
    def select(a, k):
        while True:
            n = len(a)
            if n <= 25:
                return sorted(a)[k]
            m = [sorted(a[i:i + 5])[len(a[i:i + 5]) // 2] for i in range(0, n, 5)]
            p = select(m, len(m) // 2)
            l, h = [_ for _ in a if _ < p], [_ for _ in a if _ > p]
            if k < len(l):
                a = l
            elif k < n - len(h):
                return p
            else:
                k -= n - len(h)
                a = h
    if n % 2:
        print(select(a, n // 2))
    else:
        print(select(a, (n - 1) // 2), select(a, n // 2))
if t == 5:  # counting sort, O(n)
    c, r = [0] * 900, []
    for i in a:
        if 100 <= i <= 999:
            c[i - 100] += 1
    for _, i in enumerate(c):
        if i:
            r.extend([_+100] * i)
    print(*r)
