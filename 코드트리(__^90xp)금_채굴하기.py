n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.
max_val = 0
for i in range(n):
    for j in range(n):
        for k in range(n + 1):
            gold_cnt = sum(
                grid[i + di][j + dj]
                for di in range(-k, k + 1)
                for dj in range(-k, k + 1)
                if 0 <= i + di < n 
                and 0 <= j + dj < n 
                and abs(di) + abs(dj) <= k
            )
            
            if gold_cnt * m >= k ** 2 + (k + 1) ** 2:
                max_val = max(max_val, gold_cnt)

print(max_val)