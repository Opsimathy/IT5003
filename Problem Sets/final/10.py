n, k = map(int, input().split())
m = (n - 1) // k
print(min(n - 1, k + 1 + (n - 1 - m * k) if m >= 2 else n - 1))
