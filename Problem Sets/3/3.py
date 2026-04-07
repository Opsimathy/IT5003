# Matric Number: A0332008U
# Name: Li Jiaru
# Lab Group Number: B3B
# Lab TA Name: Manish Choudhary

a = [input() for _ in range(int(input()))]
p, f = [], set()
for c in a:
    if c == "cd ..":
        p.pop()
    elif c[0] == "c":
        p.append(c[3:])
    else:
        f.add("/".join(p + [c[5:]]))
for _ in sorted(f):
    print("git add", _)
print("git commit\ngit push")
