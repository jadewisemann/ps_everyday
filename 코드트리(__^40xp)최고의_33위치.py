n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.
max_val = 0
for i in range(0, n - 2):
    for j in range(0, n - 2):
        tmp_sum = sum(sum(row[j:j+3]) for row in grid[i:i+3])
        if max_val < tmp_sum:
            max_val = tmp_sum
            
print(max_val)

