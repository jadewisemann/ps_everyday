for tc in range(int(input())):
    n = int(input())
    carots = list(map(int, input().split()))

    ttl_sum = sum(carots)
    sums, diffs = [0] * (n + 1), [0] * (n + 1)
    min_idx, min_diff = None, float('inf')

    for i in range(1, n + 1):
        sums[i] = sums[i - 1] + carots[i - 1]
        diffs[i] = ttl_sum - sums[i] * 2
        if abs(diffs[i]) < min_diff:
            min_diff = abs(diffs[i])
            min_idx = i
    
    print(f'#{tc + 1} {min_idx} {min_diff}')