# from 12 to clock wise 8 => r: 2, l: 6
gears = [
    list(map(int, input()))
    for _ in range(4)
]

pos = [0] * 4

l_pos = lambda i: (pos[i] + 6) % 8
r_pos = lambda i: (pos[i] + 2) % 8

for _ in range(int(input())):
    num, dir = map(int, input().split())
    num -= 1

    move = [0] * 4
    move[num] = dir

    # propagate to left
    for i in range(num, 0, -1): 
        if gears[i][l_pos(i)] != gears[i - 1][r_pos(i - 1)]:
            move[i - 1] = move[i] * (-1)
        else: break
    
    # propaget to right
    for i in range(num, 3):
        if gears[i][r_pos(i)] != gears[i + 1][l_pos(i + 1)]:
            move[i + 1] = move[i] * (-1)
        else: break

    # rotate
    for i in range(4):
        if move[i]:
            pos[i] = (pos[i] - move[i]) % 8

print(sum(
    gears[i][pos[i]] * (2**i)
    for i in range(4)
))
