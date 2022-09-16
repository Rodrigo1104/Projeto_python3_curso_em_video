s = 0
c_u = 0
for c in range(0, 500):
    if c % 3 == 0 and c % 2 != 0:
        c_u += 1
        s += c
print(s, c_u)
