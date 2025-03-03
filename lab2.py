C = [0, 1, -2, 6, -7, 8, 13, 106, -256, 122]
S = 0
n = len(C)

for i in range(0, n):
    if C[i] > 0:
        S = S + C[i]
    i = i + 1

print(S)
