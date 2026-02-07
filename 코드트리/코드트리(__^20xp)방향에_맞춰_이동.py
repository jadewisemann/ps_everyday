n = int(input())
moves = [tuple(input().split()) for _ in range(n)]
dir = [move[0] for move in moves]
dist = [int(move[1]) for move in moves]

# Please write your code here.

DIRS = {
    'N': (0,  1),
    'S': (0, -1),
    'E': ( 1, 0),
    'W': (-1, 0)
}
ix, iy = 0, 0
for idx in range(n):
    dx, dy = DIRS[dir[idx]]
    ix += dx * dist[idx]
    iy += dy * dist[idx]

print(ix, iy)