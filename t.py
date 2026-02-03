for tc in range(10):
    towers = [0] * 101
    n = int(input())
    min_pointer, max_pointer = 101, 0
    for tower in map(int, input().split()):
        towers[tower] += 1
        if tower > max_pointer:
            max_pointer = tower
        if tower < min_pointer:
            min_pointer = tower

    for _ in range(n):
        towers[max_pointer] -= 1
        towers[max_pointer - 1] += 1
        if towers[max_pointer] == 0:
            max_pointer -= 1

        towers[min_pointer] -= 1
        towers[min_pointer + 1] += 1
        if towers[min_pointer] == 0:
            min_pointer += 1
    
    print(f'#{tc + 1} {max_pointer - min_pointer}')