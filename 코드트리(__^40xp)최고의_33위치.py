n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.
max_val = 0
for i in range(0, n - 2):
    for j in range(0, n - 2):
        
        tmp = 0
        for r in range(3):
            for c in range(3):
                tmp += grid[i + r][j + c]

        if max_val < tmp:
            max_val = tmp
print(max_val)

