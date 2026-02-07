ip = lambda: map(int, input().split())

n, s = ip()
arr = list(ip())

def dfs(idx, current_sum):
    if idx == n:
        return 1 if current_sum == s else 0
    
    return dfs(idx + 1, current_sum + arr[idx]) + dfs(idx + 1, current_sum)

print(dfs(0, 0) - (1 if s == 0 else 0))