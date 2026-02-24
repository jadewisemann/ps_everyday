w, h  = map(int, input().split())

w_cut = [0, w] 
h_cut = [0, h]

n = int(input())

for _ in range(n):
  dir, coord = map(int, input().split())
  if dir == 0:
    h_cut.append(coord)
  else:
    w_cut.append(coord)
  
w_cut.sort()
h_cut.sort()

wm = 0
tmp = 0
for cut in w_cut:
  wm = max(cut-tmp, wm)
  tmp = cut

hm = 0
tmp = 0
for cut in h_cut:
  hm = max(cut-tmp, hm)
  tmp = cut

print(wm * hm)