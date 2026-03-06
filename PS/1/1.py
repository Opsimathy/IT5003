# Matric Number: A0332008U
# Name: Li Jiaru
# Lab Group Number: B3B
# Lab TA Name: Manish Choudhary

T = H = 0
for i in input():
    if i == 'T':
        T += 1
    elif i == 'H':
        H += 1
    if T >= 11 and T - H >= 2 or H >= 11 and H - T >= 2:
        T = H = 0
print(f"{T}-{H}")
