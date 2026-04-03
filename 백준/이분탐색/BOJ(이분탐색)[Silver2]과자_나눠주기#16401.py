m, n = map(int, input().split())
snacks = list(map(int, input().split()))

start = 1
end = max(snacks)
answer = 0

while start <= end:
    mid = (start + end) // 2

    count = sum(snack // mid for snack in snacks)

    if count >= m:
        answer = mid
        start = mid + 1
    else:
        end = mid - 1

print(answer)



