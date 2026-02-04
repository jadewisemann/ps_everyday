for tc in range(int(input())):

    rsx, rsy, rex, rey = map(int, input().split())
    bsx, bsy, bex, bey = map(int, input().split())

    isx = max(rsx, bsx)
    iex = min(rex, bex)

    isy = max(rsy, bsy)
    iey = min(rey, bey)

    w, h = 0, 0

    if isx <= iex and isy <= iey:
        w = iey - isy + 1
        h = iex - isx + 1

    print(f'#{tc + 1} {w} {h}')