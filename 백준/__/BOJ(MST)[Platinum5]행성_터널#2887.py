import sys
sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline


def find(parent, x):
    if parent[x] != x:
        parent[x] = find(parent, parent[x])
    
    return parent[x]


def union(parent, a, b):
    root_a = find(parent, a)
    root_b = find(parent, b)

    if root_a == root_b:
        return False

    if root_a < root_b:
        parent[root_b] = root_a
    else:
        parent[root_a] = root_b
    return True


n = int(input())
planets = [
    (*map(int, input().split()), i)
    for i in range(n)
]


edges = []
for axis in range(3):
    planets.sort(key= lambda p: p[axis])
    for i in range(n - 1):
        cost = abs(planets[i][axis] - planets[i + 1][axis])
        edges.append((cost, planets[i][3], planets[i + 1][3]))

edges.sort()


parent = [i for i in range(n)]
global_min, tunnel_count = 0, 0

for cost, a, b in edges:
    if union(parent, a, b):
        global_min += cost
        tunnel_count += 1

        if tunnel_count == n - 1: break


print(global_min)