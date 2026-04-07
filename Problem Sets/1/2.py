# Matric Number: A0332008U
# Name: Li Jiaru
# Lab Group Number: B3B
# Lab TA Name: Manish Choudhary

n = int(input())
s = input()[::-1]
G = A = 0
max_G = max_A = 0
for i in s:
    if i == 'G':
        G += 1
    elif i == 'A':
        A += 1
    if G + A == 0:
        continue
    elif max_G + max_A == 0 or G * (max_G + max_A) > max_G * (G + A):
        max_G, max_A = G, A
print(f"{max_G}-{max_A}")
