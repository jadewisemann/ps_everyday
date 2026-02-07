squares = [list(map(int, input().split())) for _ in range(4)]

visited  = []
for square in squares:
  sx, sy, ex, ey = square
  
  for i in range(sx,ex):
    for j in range(sy, ey):
      if [i, j] in visited:
        continue
      visited.append([i,j])

print(len(visited))
