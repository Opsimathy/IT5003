# Matric Number: A0332008U
# Name: Li Jiaru
# Lab Group Number: B3B
# Lab TA Name: Manish Choudhary

n = int(input())
t = sorted([int(input()) for _ in range(n)])
print(min((i+1) * t[i] + (n-i-1) * t[-1] for i in range(n)) - sum(t))
