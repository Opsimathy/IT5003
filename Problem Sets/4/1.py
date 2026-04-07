# Matric Number: A0332008U
# Name: Li Jiaru
# Lab Group Number: B3B
# Lab TA Name: Manish Choudhary

n, m = map(int, input().split())
a = [0] * 7
for _ in range(n):
    a[int(input())] += 1
print("Nej" if n - max(a) > m else "Ja")
