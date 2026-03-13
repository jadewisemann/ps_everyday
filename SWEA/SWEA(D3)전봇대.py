# for tc in range(int(input())):
#     n = int(input())
#     lines = sorted(
#         [
#             list(map(int, input().split()))
#             for _ in range(n)
#         ]
#     )
#     ans = sum(
#         1
#         for i in range(n)
#         for j in range(i + 1, n)
#         if lines[i][1] > lines[j][1]
#     )
            
#     print(f"#{tc + 1} {ans}")

for tc in range(int(input())):
    n = int(input())
    lines = sorted(
        [
            tuple(map(int, input().split()))
            for _ in range(n)    
        ]
    )

    tree = [0] * 10001
    ans = 0
    
    for _, b in reversed(lines):
        i = b - 1
        while i > 0:
            ans += tree[i]
            i -= (i & -i)
        
        i = b
        while i <= 10000:
            tree[i] += 1
            i += (i & -i)
            
    print(f"#{tc + 1} {ans}")