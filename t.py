# Read 4x4 grid
grid = [list(map(int, input().split())) for _ in range(4)]

# Read direction
dir = input()

# code here

def rotate(grid):
    return [list(row[::-1]) for row in zip(*grid)]
    
def push_left(grid):
    new_grid = []
    for row in grid:
        nums = [val for val in row if val != 0]
        merged = []
        idx =  while idx < len(nums):
            if idx + 1 < len(nums) and nums[idx] == nums[idx+1]:
                merged.append(nums[idx] * 2)
                idx += 2
            else:
                merged.append(nums[idx])
                idx += 1
        new_grid.append(merged + [0] * (4 - len(merged)))
    return new_grid

rotate_count = {'L': 0, 'D': 1, 'R': 2, 'U': 3}[dir]

for _ in range(rotate_count):
    grid = rotate(grid)
    
grid = push_left(grid)

for _ in range((4 - rotate_count) % 4):
    grid = rotate(grid)
    
for row in grid:
    print(*(row))
