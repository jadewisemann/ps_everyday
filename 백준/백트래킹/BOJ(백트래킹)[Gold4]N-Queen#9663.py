
def dfs(row, n, v1, v2, v3):
    if row == n:
        return 1
    
    count = 0

    for col in range(n):
        if v1[col] or v2[row + col] or v3[row - col + n - 1]:
            continue
            
        v1[col] = True
        v2[row + col] = True
        v3[row - col + n - 1] = True
        
        count += dfs(row + 1, n, v1, v2, v3)
        
        v1[col] = False
        v2[row + col] = False
        v3[row - col + n - 1] = False
        
    return count

n = int(input())

v1 = [False] * n              
v2 = [False] * (2 * n)        
v3 = [False] * (2 * n)        

print(dfs(0, n, v1, v2, v3))