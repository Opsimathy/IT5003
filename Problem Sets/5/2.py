# Matric Number: A0332008U
# Name: Li Jiaru
# Lab Group Number: B3B
# Lab TA Name: Manish Choudhary

n = int(input().split()[0])
p1 = list(map(int, input().split()))
input()
p2 = list(map(int, input().split()))
c, s, j = [[] for _ in range(n + 1)], [], 0
for i in p1:
    if s:
        c[s[-1]].append(i)
    s.append(i)
    while s and s[-1] == p2[j]:
        s.pop()
        j += 1
for i in range(1, n + 1):
    print(f"{i}:", *c[i])
