# Matric Number: A0332008U
# Name: Li Jiaru
# Lab Group Number: B3B
# Lab TA Name: Manish Choudhary

k, n = int(input()), int(input())
p = [(int(w), _, i) for _ in range(n) for i, w in [input().split()]]
p.sort()
w = [x[0] for x in p]
a = n // k
b = -(-n // k)
if sum(w[:b]) < sum(w[b:a+b]):
    a = b
p = p[:a]
print(sum(x[0] for x in p))
for i in sorted(x[2] for x in p):
    print(i)
