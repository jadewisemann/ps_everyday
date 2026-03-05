def get_data():
    n = int(input())
    adj = [[] for _ in range(n + 1)]       
    indegree = [0] * (n + 1)
    durations = [0] * (n + 1)

    for i in range(1, n + 1):
        time, _, *precedents = map(int, input().split())
        durations[i] = time

        for pre in precedents:
            adj[pre].append(i)
            indegree[i] += 1

    return n, adj, indegree, durations

def get_topological_order(n, adj, indegree):
    _indegree = indegree[:]
    
    queue = [0] * (n + 1)
    head = tail = 0
    
    for i in range(1, n + 1):
        if _indegree[i] == 0:
            queue[tail] = i
            tail += 1

    while head < tail:
        curr = queue[head]
        head += 1
        for nxt in adj[curr]:
            _indegree[nxt] -= 1
            if _indegree[nxt] == 0:
                queue[tail] = nxt
                tail += 1
    
    return queue[:tail] if tail == n else []

def solve(order, precedents, current_durations):
    dp = [0] * (len(order) + 1)

    for curr in order:
        max_pre_time = 0
        for pre in precedents[curr]:
            max_pre_time = max(max_pre_time, dp[pre])

            dp[curr] = max_pre_time + current_durations[curr]

    return max(dp) if dp else 0

def main():
    for tc in range(int(input())):
        n, adj, precedents, indegree, durations = get_data()
        order = get_topological_order(n, adj, indegree)
        if not order: 
            print(-1)
            return
        
        ans = solve(order, precedents, durations)

        durations[i] = 

        answer = solve()
        print(f'{tc + 1} {}')


if __name__ == "__main__":
    main()