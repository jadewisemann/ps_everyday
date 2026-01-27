from collections import deque

qu  = deque([])
grp = []
vis = []
while qu:
    sx, sy  = qu.popleft()
    vis.append([sx, sy])
    # 종료조건?
        # 탐색하거나 
    
    # 방향순회

    for dx, dy in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
        nx, ny = sx + dx, sy + dy

        # 경계값
        if 0 <= nx < n and 0<= ny <m:
            if [nx, ny] in vis:
                continues
            # 이것저것

            qu.append([nx,ny])