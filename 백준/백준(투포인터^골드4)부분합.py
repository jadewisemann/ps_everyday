n, s = map(int, input().split())
arr = list(map(int, input().split()))

l, r, curr_sum, min_len = 0, 0, 0, n + 1

while True:
    if curr_sum >= s:
        if min_len > r - l:
            min_len = r - l
        curr_sum -= arr[l]
        l += 1
    elif r >= n:
        break
    else:
        curr_sum += arr[r]
        r += 1

print(min_len if min_len != n + 1 else 0)