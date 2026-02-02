T = int(input())

for tc in range(1, T + 1):
    n = int(input())
    boxes = list(map(int, input().split()))

    global_max = 0
    for i in range(n):
        curr = boxes[i]
        local_max = 0
        for j in range(i, n):
            if curr > boxes[j]:
                local_max += 1
        if local_max > global_max:
            global_max = local_max

    print(f'#{tc} {global_max}')