dirs = input()

# Please write your code here.
x, y, dir = 0, 0, 0

for d in dirs:
    if d == 'F':
        dx, dy = [[0, 1], [1, 0], [0, -1], [-1, 0]][dir]
        x += dx
        y += dy
    elif d == 'R':
        dir = (dir + 1) % 4
    elif d == 'L':
        dir = (dir - 1) % 4

print(x, y)        