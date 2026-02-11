

n, m, q = map(int, input().split())

# Create 2D array for building state
a = [list(map(int, input().split())) for _ in range(n)]

# Process wind queries
winds = [tuple(map(int, input().split())) for _ in range(q)]

# Please write your code here.
for wind in winds:
    ax, ay, bx, by = map(lambda x: x - 1, wind)
    tmp = a[ax][ay]

    for i in range(ax, bx):
        a[i][ay] = a[i + 1][ay]

    for j in range(ay, by):
        a[bx][j] = a[bx][j + 1]

    for i in range(bx, ax, -1):
        a[i][by] = a[i - 1][by]

    for j in range(by, ay, -1):
        a[ax][j] = a[ax][j - 1]

    a[ax][ay + 1] = tmp

    copied = [row[:] for row in a]

    for i in range(ax, bx + 1):
        for j in range(ay, by + 1):
            a[i][j] = (lambda x: sum(x) // len(x))([
                copied[i + di][j + dj]
                for di, dj in ((- 1, 0), (1, 0), (0, - 1), (0, 1))
                if 0 <= i + di < n and 0 <= j + dj < m
                ] + [copied[i][j]]
            )
            
for row in a:
    print(*row)