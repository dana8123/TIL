def baetrang_num(n):
    prime_num = int(n ** 0.5)
    count = 0
    for i in (2, 2*n+1):
        if i in prime_num:
            count += 1
    return n != 1
