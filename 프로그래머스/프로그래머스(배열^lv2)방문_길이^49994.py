DIRS = {
    "U": ( 0,  1),
    "D": ( 0, -1),
    "R": ( 1,  0),
    "L": (-1,  0),
}

def solution(dirs):
    vis = set()
    sx, sy = 0, 0

    for dir in dirs:
        dx, dy = DIRS[dir]
        nx, ny = sx + dx, sy + dy
        if nx < -5 or nx > 5 or ny < -5 or ny > 5:
            continue
        vis.add((sx,sy, nx, ny))    
        vis.add((nx, ny, sx, sy))
        sx, sy = nx, ny
        
    return len(vis) // 2