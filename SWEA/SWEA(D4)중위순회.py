def in_order(v):
    global result
    if v <= n:
        in_order(v * 2)
        result += tree[v]
        in_order(v * 2 + 1)

for tc in range(1, 11):
    line = input()
    n = int(line)

    tree = [0] * (n + 1)
    
    for _ in range(n):
        info = input().split()
        idx = int(info[0])
        char = info[1]
        tree[idx] = char
    
    result = ""
    in_order(1)
    
    print(f"#{tc} {result}")