# Matric Number: A0332008U
# Name: Li Jiaru
# Lab Group Number: B3B
# Lab TA Name: Manish Choudhary

t = {"Skrimsli": 0, "Galdur": 1, "Gildra": 2, "Annad": 3}
s = {"Skrimsli": {"Venjulegt": 0, "Ahrifa": 1, "Bodunar": 2, "Samruna": 3,
                  "Samstillt": 4, "Thaeo": 5, "Penduls": 6, "Tengis": 7},
     "Galdur": {"Venjulegur": 0, "Bunadar": 1, "Svida": 2, "Samfelldur": 3,
                "Bodunar": 4, "Hradur": 5},
     "Gildra": {"Venjuleg": 0, "Samfelld": 1, "Mot": 2},
     "Annad": {}}

n = int(input())
a = []
for _ in range(n):
    na, i, f, d = input().split(", ")
    if " - " in f:
        f1, f2 = f.split(" - ")
        f = (t[f1], s[f1][f2])
    else:
        f = (t[f], -1)
    a.append({"nafn": na, "id": int(i), "flokkur": f, "dagsetning": d})
o = input().split()
a.sort(key=lambda c: [c[k] for k in o])
for c in a:
    print(c["nafn"])
