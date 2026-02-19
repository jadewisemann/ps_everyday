import sys
input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())

    selections = [0] + list(map(int, input().split()))
    visited = [False] * (n + 1)
    team_member_count = 0
    
    for i in range(1, n + 1):
        if visited[i]:
            continue

        curr = i
        path = []
        path_set = set()
        
        while not visited[curr]:
            visited[curr] = True
            path.append(curr)
            path_set.add(curr)
            curr = selections[curr]
        
        if curr in path_set:
            idx = path.index(curr)
            team_member_count += len(path) - idx
    
    print(n - team_member_count)