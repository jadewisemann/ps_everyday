def calculate(node_idx):
    node = tree[node_idx]
    
    if len(node) == 2:
        return float(node[1])
    
    left_val = calculate(int(node[2]))
    right_val = calculate(int(node[3]))
    op = node[1]
    
    if op == '+': return left_val + right_val
    if op == '-': return left_val - right_val
    if op == '*': return left_val * right_val
    if op == '/': return left_val / right_val

for tc in range(1, 11):
    N = int(input())
        
    tree = [None] * (N + 1)
    for _ in range(N):
        info = input().split()
        tree[int(info[0])] = info
        
    result = calculate(1)
    print(f"#{tc} {int(result)}")