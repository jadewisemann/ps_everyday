n, k = map(int, input().split())
coins = [int(input()) for _ in range(n)]

# Please write your code here.
coins.sort(reverse=True)

curr = 0
count = 0
for coin in coins:
    while curr + coin <= k:
        curr += coin
        count += 1
    if curr == k:
        break

print(count)
