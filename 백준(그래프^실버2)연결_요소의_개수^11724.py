import sys
input = sys.stdin.readline

ip = lambda:  map(int, input().split())

n, m = ip()

roots = list(range(n+1))

def find(x):

    root  = x
    while roots[root] != root:
        root = roots[root]

    curr = x
    while roots[curr] != root:
        next = roots[curr]
        roots[curr] = root
        curr = next

    return root

for _ in range(m):
    u, v = ip()

    ru, rv = find(u), find(v)
    if ru != rv:
        roots[rv] = ru
    
print(sum(1 for i in range(1, n+1) if roots[i] == i))
