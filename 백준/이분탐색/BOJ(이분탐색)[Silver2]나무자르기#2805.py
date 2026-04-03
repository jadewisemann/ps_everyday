n, m = map(int, input().split())
heights = list(map(int, input().split()))

end = max(heights)
start = 0
rst = 0

while start <= end:
    mid = (start + end) // 2
    total = sum(h - mid  if h > mid else 0 for h in heights)


    if total < m:
        end = mid - 1
    else:
        rst = mid
        start = mid + 1

print(rst)