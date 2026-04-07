# Matric Number: A0332008U
# Name: Li Jiaru
# Lab Group Number: B3B
# Lab TA Name: Manish Choudhary

n, m = map(int, input().split())
a = set()
for _ in range(n):
    a |= set(map(int, input().split()[1:]))
print("Jebb" if all(i in a for i in range(1, m + 1)) else "Neibb")
