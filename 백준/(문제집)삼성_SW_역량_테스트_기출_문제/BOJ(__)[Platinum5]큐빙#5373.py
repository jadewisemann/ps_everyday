def rotate_90(matrix, clockwise):
    if clockwise: return [list(row) for row in zip(*matrix[::-1])]
    else:         return [list(row) for row in zip(*matrix)][::-1]

def get_side(cube, side_idx, pos):
    face = cube[side_idx]
    idx = int(pos[1])

    if pos.startswith('r'): return face[idx][:]
    else:                   return [face[i][idx] for i in range(3)]

def set_side(cube, side_idx, pos, values):
    face = cube[side_idx]
    idx = int(pos[1])
    
    if pos.startswith('r'): face[idx] = values;       return
    for i in range(3):      face[i][idx] = values[i]


def transform(cube, side_idx, clockwise, adj_info):
    cube[side_idx] = rotate_90(cube[side_idx], clockwise)
    
    sides =         [info[0] for info in adj_info]
    positions =     [info[1] for info in adj_info]
    reverse_flags = [info[2] for info in adj_info]
        
    current_values = [
        get_side(cube, sides[i], positions[i])[::-1 if reverse_flags[i] else 1]
        for i in range(4)
    ]
        
    if clockwise: new_values = [current_values[3]] + current_values[:3]
    else:         new_values = current_values[1:] + [current_values[0]]
    
    for side, pos, flag, val in zip(sides, positions, reverse_flags, new_values):
        set_side(cube, side, pos, val[::-1 if flag else 1])


def solve(ADJS, MAPPING):
    _ = int(input())
    ops = input().split()

    cube = [
        [list(color * 3) for _ in range(3)]
        for color in "wyrogb"
    ]
    
    for op in ops:
        side_char, direction, *_ = op
        transform(cube, MAPPING[side_char], direction == '+', ADJS[side_char])

    return cube[0]

def main():
    ADJS = {
        'U': [(3, 'r0', False), (5, 'r0', False), (2, 'r0', False), (4, 'r0', False)],
        'D': [(2, 'r2', True),  (5, 'r2', True),  (3, 'r2', True),  (4, 'r2', True)],
        'F': [(0, 'r2', True),  (5, 'c0', True),  (1, 'r0', False), (4, 'c2', False)],
        'B': [(0, 'r0', False), (4, 'c0', True),  (1, 'r2', True),  (5, 'c2', False)],
        'L': [(0, 'c0', True),  (2, 'c0', True),  (1, 'c0', True),  (3, 'c2', False)],
        'R': [(0, 'c2', False), (3, 'c0', True),  (1, 'c2', False), (2, 'c2', False)]
    }
    MAPPING = {'U':0, 'D':1, 'F':2, 'B':3, 'L':4, 'R':5}

    for _ in range(int(input())):
        rst = solve(ADJS, MAPPING)
        for row in rst:
            print("".join(row)) 

if __name__ == "__main__":
    main()