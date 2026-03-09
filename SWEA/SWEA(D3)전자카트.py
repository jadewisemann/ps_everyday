def get_input():
    n = int(input())
    adj_matrix = [
        list(map(int, input().split()))
        for _ in range(n)
    ]
    return n, adj_matrix

def solve():
    n, adj_matrix = get_input()

    visited = [False] * n 
    min_battery = float('inf')

    def dfs(curr, cnt, acc):
        nonlocal min_battery

        if acc >= min_battery: return

        if cnt  == n - 1:
            acc += adj_matrix[curr][0]
            if acc < min_battery:
                min_battery = acc
            return
        
        for nxt in range(1, n):
            if visited[nxt]: continue
            
            visited[nxt] = True
            dfs(nxt, cnt + 1, acc + adj_matrix[curr][nxt])
            visited[nxt] = False

    visited[0] = True
    dfs(0, 0, 0) 
    return min_battery


def solve_dp():
    n, adj_matrix = get_input()
    
    memo = [[-1] * (1 << n) for _ in range(n)]

    def tsp(curr, visited):
        if visited == (1 << n) - 1: 
            return adj_matrix[curr][0]

        if memo[curr][visited] != -1:
            return memo[curr][visited]

        res = float('inf')
        for nxt in range(1, n):
            if not (visited & (1 << nxt)):
                cost = tsp(nxt, visited | (1 << nxt)) + adj_matrix[curr][nxt]
                if cost < res:
                    res = cost
        
        memo[curr][visited] = res
        return res
    
    return tsp(0, 1)


def main():
    for tc in range(int(input())):
        ans = solve_dp()
        print(f'#{tc + 1} {ans}')

if __name__ == "__main__":
    main()