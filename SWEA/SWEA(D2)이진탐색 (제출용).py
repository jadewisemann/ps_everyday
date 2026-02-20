def make_bst(n):
    if n <= N:
        make_bst(n * 2)
        
        global cnt
        tree[n] = cnt
        cnt += 1
        
        make_bst(n * 2 + 1)


for tc in range(int(input())):
    N = int(input())
    tree = [0] * (N + 1)
    cnt = 1
    
    make_bst(1)
    
    print(f"#{tc + 1} {tree[1]} {tree[N // 2]}")