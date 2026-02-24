def solve():
    from collections import deque as dq 

    n,m = map(int, input().split())

    friends = [[] for _ in range(n + 1)]

    for _ in range(m):
        a, b = map(int, input().split())
        friends[a].append(b)
        friends[b].append(a)

    min_kevin_number = float('inf')
    min_idx = -1

    for i in range(1, n + 1):
        dists = [-1] * (n + 1)
        dists[i] = 0
        que = dq([i])

        while que:
            curr = que.popleft()
            for friend in friends[curr]:
                if dists[friend]  == -1:
                    dists[friend] = dists[curr] + 1
                    que.append(friend)
        
        kevin_number = sum(dist for dist in dists if dist > 0)

        if kevin_number < min_kevin_number:
            min_kevin_number = kevin_number
            min_idx = i

    print(min_kevin_number)

def solve__floyd_washer():
    n,m = map(int, input().split())

    INF = 101
    dist = [[INF] * (n + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        dist[i][i] = 0

    for _ in range(m):
        a, b = map(int, input().split())
        dist[a][b] = 1
        dist[b][a] = 1

    for k in range(1, n + 1):
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                via_dist = dist[i][k] + dist[k][j]
                if dist[i][j] > via_dist:
                    dist[i][j] = via_dist

    min_kevin = INF * n
    answer = 0

    for i in range(1, n + 1):
        curr_kevin = sum(dist[i][1:])
        
        if curr_kevin < min_kevin:
            min_kevin = curr_kevin
            answer = i

    print(answer)

def solve__set():
    n,m = map(int, input().split())
    adj = [set() for _ in range(n + 1)]

    for _ in range(m):
        a, b = map(int, input().split())
        adj[a].add(b)
        adj[b].add(a)

    min_kevin_number = None
    winner = -1

    for i in range(1, n + 1):
        dist = [0] * (n + 1)
        vis = {i}
        curr = {i}
        step = 1

        while curr:
            next = set()
            for node in curr:
                for neighbor in adj[node]:
                    if neighbor not in vis:
                        vis.add(neighbor)
                        next.add(neighbor)
                        dist[neighbor] = step
            curr = next
            step += 1
        
        kevin_number = sum(dist)
        if (
            min_kevin_number is None 
            or kevin_number < min_kevin_number
        ):
            min_kevin_number = kevin_number
            winner = i

    print(winner)