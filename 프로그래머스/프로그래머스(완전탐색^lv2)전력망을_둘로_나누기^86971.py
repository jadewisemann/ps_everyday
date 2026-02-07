def solution(n, wires):

    adj = [[] for _ in range(n + 1)]
    for u, v in wires:
        adj[u].append(v)
        adj[v].append(u)
    
    min_diff = float('inf')

    def dfs(curr, prev):
        nonlocal min_diff
        subtree_size = 1
        
        for neighbor in adj[curr]:
            if neighbor != prev:
                child_size = dfs(neighbor, curr)            
                diff = abs(child_size - (n - child_size))
                min_diff = min(min_diff, diff)
                
                subtree_size += child_size
                
        return subtree_size

    dfs(1, -1)
    
    return min_diff