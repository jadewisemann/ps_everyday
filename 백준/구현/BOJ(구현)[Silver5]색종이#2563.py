n = int(input())
grid = [[False] * 100 for _ in range(100)]
W, H = 10, 10

for _ in range(n):
  x, y = map(int, input().split())
  for i in range(x,x + W):
    for j in range(y, y + H):      
      grid[i][j] = True
  

count = 0
for low in grid:
  for num in low:
    if num:
      count += 1

print(count)


