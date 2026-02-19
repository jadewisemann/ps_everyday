def calc_dist(p1, p2):
    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])

for tc in range(int(input())):
    n = int(input())
    si, sj, ei, ej, *raw = map(int, input().split())
    
    start = (si, sj)
    end = (ei, ej)

    customers = []
    for i in range(0, n * 2, 2):
        customers.append((raw[i], raw[i + 1]))

    min_path = float('inf')
    visited = [False] * n

    def dfs(curr_pos, visited_cnt, current_dist):
        global min_path
        
        if current_dist >= min_path:
            return
        
        if visited_cnt == n:
            min_path = min(min_path, current_dist + calc_dist(curr_pos, end))
            return

        for i in range(n):
            if not visited[i]:
                visited[i] = True
                dfs(customers[i], visited_cnt + 1, current_dist + calc_dist(curr_pos, customers[i]))
                visited[i] = False

    dfs(start, 0, 0)

    print(f'#{tc + 1} {min_path}')