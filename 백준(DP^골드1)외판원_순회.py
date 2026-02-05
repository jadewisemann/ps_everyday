INF = float('inf')

n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

dp = [[-1] * (1 << n) for _ in range(n)]

def find_path(curr, visited):
    # 모든 도시 방문
    if visited == (1 << n) - 1:
        return grid[curr][0] if grid[curr][0] > 0 else INF
    
    # 메모이제이션, 즉시 반환
    if dp[curr][visited] != -1:
        return dp[curr][visited]
    
    # 탐색
    min_cost = INF
    for next in range(n):
        if grid[curr][next] > 0 and not (visited & (1 << next)):
            res = find_path(next, visited | (1 << next))
            min_cost = min(min_cost, grid[curr][next] + res)
    
    dp[curr][visited] = min_cost
    return min_cost

print(find_path(0, 1))    