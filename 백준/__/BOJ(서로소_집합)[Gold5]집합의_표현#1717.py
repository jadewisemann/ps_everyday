import sys
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline


def solve():
    def find(parents, x):
        if parents[x] != x:
            parents[x] = find(parents, parents[x])
        return parents[x]

    def union(root, a, b):
        root_a = find(root, a)
        root_b = find(root, b)
        
        if root_a < root_b:
            root[root_b] = root_a
        else:
            root[root_a] = root_b

    n, m = map(int, input().split())
    parents = [i for i in range(n + 1)]

    for _ in range(m):
        op, a, b = map(int, input().split())
        
        if op == 0: union(parents, a, b)

        elif op == 1:
            print(
                "YES"
                if find(parents, a) == find(parents, b) else
                "NO"
            )
if __name__ == "__main__":
    solve()