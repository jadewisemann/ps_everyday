K, N = map(int, input().split())

# Please write your code here.

def choose(curr, his):
    if curr == N + 1:
        print(" ".join(map(str,his)))
        return
    
    for i in range(1, K + 1):
        choose(curr + 1, [*his, i])
    
    return

choose(1, [])