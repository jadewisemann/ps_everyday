n, t = map(int, input().split())
r, c, d = input().split()
r, c = int(r), int(c)

# Please write your code here.
DIRS = {
    'U': (-1, 0),
    'D': (1, 0),
    'R': (0, 1),
    'L': (0, -1)
}

for _ in range(t):
    dr, dc = DIRS[d]
    nr, nc = r + dr, c + dc

    if nr < 1 or nr > n or nc < 1 or nc > n:
        if d == 'U': d = 'D'
        elif d == 'D': d = 'U'
        elif d == 'L': d = 'R'
        elif d == 'R': d = 'L'
    else:
        r, c = nr, nc

print(r, c)