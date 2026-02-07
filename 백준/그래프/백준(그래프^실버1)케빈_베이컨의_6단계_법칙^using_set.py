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



            

