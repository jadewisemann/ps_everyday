SIZE = 100

for _ in range(10):
    tc = int(input())
    grid = [list(map(int, input().split())) for _ in range(SIZE)]

    curr = complex(SIZE - 1, next(x for x in range(SIZE) if grid[SIZE - 1][x] == 2))
    dir = -1

    while curr.real > 0:
        if dir.real != 0:
            for side in (1j, -1j):
                nxt = curr + side
                if (
                    0 <= nxt.imag < SIZE
                    and grid[int(nxt.real)][int(nxt.imag)]
                ):
                    dir = side
                    break
        elif grid[int(curr.real - 1)][int(curr.imag)]:
            dir = -1
        
        curr += dir

    print(f'#{tc} {int(curr.imag)}')