n = int(input())
paper =  [list(map(int, input().split())) for _ in range(n)]

w = 0
b = 0


def cut(x, y, r):
    global w, b

    f = paper[x][y]

    for i in range(x, x + r):
        for j in range(y, y + r):
            if paper[i][j] != f:
                half = r // 2
                cut(x, y, half)
                cut(x, y + half, half)
                cut(x + half, y, half)
                cut(x + half, y + half, half)
                return
    
    if f == 0:
        w += 1
    else:
        b += 1

cut(0, 0, n)

print(w)
print(b)