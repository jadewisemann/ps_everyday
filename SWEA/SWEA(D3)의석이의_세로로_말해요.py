for tc in range(1, int(input()) + 1):
    strings = [input() for _ in range(5)]
    res = "".join(
        strings[i][j] 
        for j in range(max(len(s) for s in strings)) 
        for i in range(5) 
        if j < len(strings[i])
    )
    print(f'#{tc} {res}')