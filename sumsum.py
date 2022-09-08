def exp_sum(n):
    if n <= 0: return 0

    waystosum = [1] + [0] * n

    for i in range(1, n + 1):
        for y in range(i, n + 1):
            waystosum[y] += waystosum[y - i]
    return waystosum[-1]
