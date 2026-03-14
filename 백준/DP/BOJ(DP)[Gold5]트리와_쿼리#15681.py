import sys

sys.setrecursionlimit(10**6)

def solve():
    tokens = map(int, open(0).read().split())
    
    n = next(tokens)
    r = next(tokens)
    q = next(tokens)
    
    adj = [[] for _ in range(n + 1)]
    for _ in range(n - 1):
        u, v = next(tokens), next(tokens)
        adj[u].append(v)
        adj[v].append(u)
        
    size = [0] * (n + 1)

    def get_size(curr, prev):
        res = 1
        for neighbor in adj[curr]:
            if neighbor != prev:
                res += get_size(neighbor, curr)
        
        size[curr] = res
        return res

    get_size(r, -1)
    
    ans = [str(size[next(tokens)]) for _ in range(q)]
    
    print('\n'.join(ans))

if __name__ == "__main__":
    solve()