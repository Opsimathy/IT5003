# Matric Number: A0332008U
# Name: Li Jiaru
# Lab Group Number: B3B
# Lab TA Name: Manish Choudhary

n, q = map(int, input().split())
names = input().split()
queries = []
score = {name: 0 for name in names}
scores = [0]

for i in range(q):
    query = input().split()
    if query[0] == '?':
        queries.append(query)
    elif query[0] == '!':
        changes = []
        for j in range(int(query[1])):
            name = query[2 + 2 * j]
            change = int(query[3 + 2 * j])
            changes.append((name, change))
            score[name] += change
            scores.append(score[name])
        queries.append(('!', changes))


class Fenwick:
    def __init__(self, n):
        self.n = n
        self.b = [0] * (n + 1)

    def add(self, i, j):
        while i <= self.n:
            self.b[i] += j
            i += i & -i

    def sum(self, i):
        s = 0
        while i > 0:
            s += self.b[i]
            i -= i & -i
        return s


score = {name: 0 for name in names}
scores = sorted(set(scores))
fenwick = Fenwick(len(scores))
indices = {score: i + 1 for i, score in enumerate(scores)}
fenwick.add(indices[0], n)

for query, n in queries:
    if query == '?':
        s = score[n]
        print(fenwick.sum(indices[s] - 1) + 1, s)
    elif query == '!':
        for name, change in n:
            s = score[name]
            fenwick.add(indices[s], -1)
            fenwick.add(indices[s + change], +1)
            score[name] = s + change
