def find(parents, x):
    if x == parents[x]:
        return x
    
    parents[x] = find(parents, parents[x])
    return parents[x]

def union(parents, gate):
    root_gate = find(parents, gate)

    if root_gate == 0:
        return False
    else:
        parents[root_gate] = find(parents, root_gate - 1)
        return True

import sys
input = sys.stdin.readline

g, p = int(input()), int(input())

highest_gate_possible = [i for i in range(g + 1)]
count = 0

for _ in range(p):
    gi = int(input())
    if union(highest_gate_possible, gi):
        count += 1
    else:
        break

print(count)