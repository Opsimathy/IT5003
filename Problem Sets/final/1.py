n = int(input())
a = list(map(int, input().split()))
L = [i - 1 for i in range(n)]
R = [i + 1 for i in range(n)]
R[-1] = -1
alive = [1] * n
leave = [0] * n
def bad(i):
    return L[i] != -1 and alive[L[i]] and a[L[i]] > a[i] or R[i] != -1 and alive[R[i]] and a[R[i]] > a[i]
cur = [i for i in range(n) if bad(i)]
for i in cur:
    leave[i] = 1
ans = []
while cur:
    ans.append([a[i] for i in cur])
    nxt = []
    for i in cur:
        l, r = L[i], R[i]
        if l != -1:
            R[l] = r
        if r != -1:
            L[r] = l
        alive[i] = 0
        for j in (l, r):
            if j != -1 and alive[j] and not leave[j] and bad(j):
                leave[j] = 1
                nxt.append(j)
    cur = nxt
print(len(ans))
for i in ans:
    print(*i)
print(*(a[i] for i in range(n) if alive[i]))
