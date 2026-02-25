n = int(input())
grid = [
    list(map(int, input().split()))
    for _ in range(n)
]

count_dict = {-1 : 0, 0 : 0, 1: 0 }

def recur(x, y, n):
    curr  = grid[x][y]
    for i in range(x, x + n):
        for j in range(y, y + n):
            if curr == grid[i][j]: continue
            m = n // 3
            
            [
                recur(x + i * m, y + j * m, m)
                for i in range(3)
                for j in range(3)
            ]

            return
        
    count_dict[curr] += 1    

recur(0, 0, n)

print(*count_dict.values(), sep="\n")