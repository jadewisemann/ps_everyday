n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.
BOMB = {
    1: (
        ( 2, 0),
        ( 1, 0),
        (-1, 0),
        (-2, 0),
        ( 0, 0)
    ),
    2: (
        ( 1,  0),
        (-1,  0),
        ( 0,  1),
        ( 0, -1),
        ( 0,  0)
    ),
    3: (
        ( 1,  1),
        (-1,  1),
        ( 1, -1),
        (-1, -1),
        ( 0,  0)
    )
}

bombs = []
num_bombs = 0

for i in range(n):
    for j in range(n):
        if grid[i][j] == 1:
            bombs.append((i, j))
            num_bombs += 1            
    
rst = []
def bombing(curr):
    if len(curr) >= num_bombs:
        cnt = 0

        grp = [[0] * n for _ in range(n)]
        for (i, j), b in zip(bombs, curr):
            
            for di, dj in BOMB[b]:
                ni, nj = i + di, j + dj
                if ni < 0 or ni >= n or nj < 0 or nj >= n:
                    continue
                if grp[ni][nj] != 0:
                    continue
                grp[ni][nj] = 1
                cnt += 1

        rst.append(cnt)
        
        return
    bombing([*curr, 1])
    bombing([*curr, 2])
    bombing([*curr, 3])

bombing([])
 
print(max(rst))