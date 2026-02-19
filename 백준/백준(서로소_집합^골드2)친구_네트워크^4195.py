import sys
input = sys.stdin.readline

def find(x, parents):
    if parents[x] == x:
        return x
    
    parents[x] = find(parents[x], parents) 
    return parents[x]

def union(x, y, parents, count):
    root_x = find(x, parents)
    root_y = find(y, parents)

    if root_x != root_y:
        parents[root_y] = root_x
        count[root_x] += count[root_y]
    
    return count[root_x]

def solve():
    parents = {}
    count = {}

    for _ in range(int(input())):
        a, b = input().split()
        
        for person in [a, b]:
            if person not in parents:
                parents[person] = person
                count[person] = 1

        print(union(a, b, parents, count))

for tc in range(int(input())):
    solve()