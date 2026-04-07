# Matric Number: A0332008U
# Name: Li Jiaru
# Lab Group Number: B3B
# Lab TA Name: Manish Choudhary

l = int(input().replace('.', ''))
s = int(input().replace('.', ''))
ans = c = 0
for i in range(12):
    x = int(input())
    x -= x * l // 10000 + x * s // 10000
    b1 = min(x, 409986)
    b2 = min(max(x - 409986, 0), 741026)
    b3 = max(x - 1151012, 0)
    w = (b1 * 3145 + b2 * 3795 + b3 * 4625) // 10000
    a = c + 59665
    c = max(0, a - w)
    ans += x - max(0, w - a)
print(ans)
