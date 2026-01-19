# 동서남부 
# 1234

n = int(input())
xs = []
ys = []

for _ in range(6):
  dir, dist = map(int, input().split())
  print(f'dir is {dir}, dist is {dist}')
  if dir == 2 or 4:
    xs.append(dist)
  elif dir == 3 or 1:
    ys.append(dist)

print(max(xs) * max(ys) - min(xs) * min(ys))
