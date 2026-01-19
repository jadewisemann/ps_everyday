
k = int(input())

mw, mh, mwi, mhi = 0, 0, 0, 0
arr = []

for i in range(6):
  dir, dist = map(int, input().split())
  arr.append(dist)

  if dir == 1 or dir == 2:
    if dist > mw:
      mw = dist
      mwi = i

  elif dir == 3 or dir == 4:
    if dist > mh:
      mh = dist
      mhi = i


print((mw *  mh - (arr[(mwi + 3) % 6]) * (arr[(mhi + 3) % 6]))* k)