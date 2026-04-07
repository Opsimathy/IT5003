# Matric Number: A0332008U
# Name: Li Jiaru
# Lab Group Number: B3B
# Lab TA Name: Manish Choudhary

a = input()
s = []
f = True

for c in a:
    if c in "pgo":
        s.append(c)
    elif c in "PGO":
        while s and s[-1] != c.lower():
            s.pop()
        if not s:
            print("Neibb")
            f = False
            break
        s.pop()

if f:
    print(*(s.count(c) for c in "pgo"), sep="\n")
