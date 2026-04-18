# Matric Number: A0332008U
# Name: Li Jiaru
# Lab Group Number: B3B
# Lab TA Name: Manish Choudhary

from collections import deque
h, w = map(int, input().split())
g = [input() for _ in range(h)]
for i in range(h):
    for j in range(w):
        if g[i][j] == 'S':
            q = deque([(i, j, 1)])
            s = {(i, j)}
            break
while q:
    i, j, d = q.popleft()
    for di, dj in ((1, 0), (0, 1), (-1, 0), (0, -1)):
        ni, nj = i + di, j + dj
        if 0 <= ni < h and 0 <= nj < w and g[ni][nj] != '#' and (ni, nj) not in s:
            if g[ni][nj] == 'G':
                print(d)
                exit()
            s.add((ni, nj))
            q.append((ni, nj, d + 1))
print("thralatlega nettengdur")
