# Matric Number: A0332008U
# Name: Li Jiaru
# Lab Group Number: B3B
# Lab TA Name: Manish Choudhary

n, a, p, s, f = int(input()), input(), {"(": ")", "[": "]", "{": "}"}, [], True
for i, c in enumerate(a):
    if c in p:
        s.append((c, i))
    elif c in p.values():
        if not s or p[s.pop()[0]] != c:
            print(c, i)
            f = False
            break
if f:
    print("ok so far")
