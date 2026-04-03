h, w = map(int, input().split())
blocks = list(map(int, input().split()))

ans = sum(
    max(
        0,
        min(
            max(blocks[:i]),
            max(blocks[i+1:])
        ) - blocks[i]
    ) 
    for i in range(1, w - 1)
)

print(ans)