t = int(input())
paper = [list(map(int, input().split())) for _ in range(t)]
visited =  []
count = []

for idx in range(t):
    tmp_count = 0
    x, y, w, h = paper[(-1) * (idx+1)]
    for  i in range(x,x+w):
        for j in range(y, y+h):
            if [i, j] in visited:
                continue
            visited.append([i, j])
            tmp_count += 1
    count.insert(0, tmp_count)

for el in count:
    print(el)