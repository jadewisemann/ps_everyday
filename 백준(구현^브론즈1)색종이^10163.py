import sys
from itertools import islice
input = sys.stdin.readline

T = int(input())
paper = []
grid = [[0] * 1001 for _ in range(1001)]
max_x, max_y = 0, 0

for t in range(1, T+1):
    x, y, w, h = map(int, input().split())
    
    for i in range(x, x+w):
        for j in range(y, y+h):
            grid[i][j] = t

    if x + w > max_x : max_x = x + w
    if y + h > max_y : max_y = y + h

count = [0] * (T+1)

for row in islice(grid, max_x):
    for el in islice(row, max_y):
        if el != 0:
            count[el] += 1

for i in range(1, T+1):
    print(count[i])             