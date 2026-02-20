for tc in range(int(input())):
    n, m, l = map(int, input().split())
    nodes = [0] * (n + 2)

    for _ in range(m):
        leaf, value = map(int, input().split())
        nodes[leaf] = value

    for i in range(n, 0, -1):
        if not nodes[i]:
            nodes[i] = nodes[i * 2] + nodes[min(i * 2 + 1, n + 1)]
    
    print(f'#{tc + 1} {nodes[l]}')