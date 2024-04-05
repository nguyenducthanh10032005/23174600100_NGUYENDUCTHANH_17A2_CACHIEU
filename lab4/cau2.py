#2a
m = 2
while m < 100:
    m = True
    k = 2
    while k <= m // 2:
        if m % k == 0:
            m = False
            break
        k += 1
    if m:
        print(m)
    m += 1

