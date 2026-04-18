from bisect import bisect_left
n = sorted(input() for _ in range(int(input())))
for _ in range(int(input())):
    k = input()
    print(bisect_left(n, k + '{') - bisect_left(n, k))
