# 시작

# 탐색
    # 현재 뽑기

    # 머든 후보 뽑기
        # 경계값
        # 방문처리

    # 후보 넣기
end = input()
n = int(input())
start_point, end_point = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

# 시작
stack = [start_point]
visited = set()

while stack:
    current = stack.pop()

    if current == end:
        break
    
    sx, sy = current
    for dx, dy in range((1, 0), (-1, 0), (0, 1), (0, -1)):
        nx, ny = sx + dx, sy + dy
        if not(0 <= nx < n and 0 <= ny < n):
            continue
        if (nx, ny) in visited:
            continue
        if grid[nx][ny] == 1:
            continue
        stack.append((nx, ny))
        visited.add((nx, ny))




