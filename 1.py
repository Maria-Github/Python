cnt = 0
nmax = 0
for i in range(-9563, 3102):
    if i % 7 == 0 and i % 11 != 0 and i % 23 != 0 and i % 10 != 8:
        cnt += 1
        nmax = i
print(cnt, nmax)
