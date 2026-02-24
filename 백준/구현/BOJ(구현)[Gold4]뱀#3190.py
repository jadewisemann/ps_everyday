from collections import deque

# == constant ==
SNAKE = 1
APPLE = 2


# == get input ==
n = int(input()) # board size

grid = [[0] * n for _ in range(n)]
for _ in range(int(input())):
    ai, aj = map(int, input().split())
    grid[ai - 1][aj - 1] = APPLE

rotations = {}
for _ in range(int(input())):
    time, dirs = input().split()
    rotations[int(time)] = dirs


# == simulation ==
dirs_index = 0
time = 0

si, sj = 0, 0
grid[si][sj] = SNAKE

snakes = deque([(si, sj)])

while True:
    time += 1

    # get coordinate
    di, dj = ((0, 1), (1, 0), (0, -1), (-1, 0))[dirs_index]
    si, sj = si + di, sj + dj

    # boundary check
    if not (0 <= si < n and 0 <= sj < n): break
    if grid[si][sj] == SNAKE: break

    # move tail
    if grid[si][sj] != APPLE:
        ti, tj = snakes.popleft()
        grid[ti][tj] = 0

    # move head
    grid[si][sj] = SNAKE
    snakes.append((si, sj))

    # rotate
    if time in rotations:
        if rotations[time] == "L":  # levo
            dirs_index = (dirs_index - 1) % 4
        elif rotations[time] == "D": # dextro
            dirs_index = (dirs_index + 1) % 4

print(time)
