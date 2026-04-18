n, e, q = map(int, input().split())
g = [0] * (n + q)
for _ in range(e):
    a, b = map(int, input().split())
    g[a] |= 1 << b
r = c = 0
for _ in range(q):
    a = list(map(int, input().split()))
    t = a[0]
    if t == 1:
        if c:
            b = 1 << n
            g[n] = b - 1
            for i in range(n):
                g[i] |= b
        n += 1
    elif t == 3:
        x = a[1]
        b = 1 << x
        g[x] = ((1 << n) - 1) ^ b if c else 0
        for i in range(n):
            if c:
                if i != x:
                    g[i] |= b
            else:
                g[i] &= ~b
    elif t == 2 or t == 4:
        x, y = a[1], a[2]
        if r:
            x, y = y, x
        b = 1 << y
        g[x] = g[x] | b if ((t == 2) ^ c) else g[x] & ~b
    else:
        r ^= t == 5
        c ^= t == 6
print(n)
g = g[:n]
m = (1 << n) - 1
if r:
    h = [0] * n
    for i, x in enumerate(g):
        x &= m
        while x:
            b = x & -x
            h[b.bit_length() - 1] |= 1 << i
            x ^= b
    g = h
for i, x in enumerate(g):
    x = ((x & m) ^ (m if c else 0)) & ~(1 << i)
    d = x.bit_count()
    s, p = 0, 1
    while x:
        b = x & -x
        s = (s + p * (b.bit_length() - 1)) % 1000000007
        p = p * 7 % 1000000007
        x ^= b
    print(d, s)
