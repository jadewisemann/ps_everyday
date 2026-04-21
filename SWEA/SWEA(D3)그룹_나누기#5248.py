def main():
    def find(parent, x):
        if parent[x] == x: return x
        parent[x] = find(parent, parent[x])
        return parent[x]

    def union(parent, x, y):
        root_x, root_y = find(parent, x), find(parent, y)
        if root_x != root_y:
            parent[root_y] = root_x    

    for tc in range(int(input())):
        n, m = map(int, input().split())
        parent = list(range(n + 1))

        it = iter(map(int, input().split()))
        for _ in range(m):
            union(parent, next(it), next(it))
        
        ans = len({find(parent, i) for i in range(1, n + 1)})

        print(f'#{tc + 1} {ans}')


if __name__ == '__main__':
    main()