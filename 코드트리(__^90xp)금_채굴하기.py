n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.
max_val = 0

for i in range(n):
    for j in range(n):

        for k in range(n + 1):
            gold_cnt = 0

            for r in range(-k, k + 1):
                for c in range(-(k - abs(r)), k - abs(r) + 1):
                    nr, nc = i + r, j + c
                    if 0 <= nr < n and 0 <= nc < n:
                        gold_cnt += grid[nr][nc]
            
            cost = k ** 2 + (k + 1) ** 2
            revenue = gold_cnt * m

            if revenue >= cost:
                max_val = max(max_val, gold_cnt)

print(max_val)

            