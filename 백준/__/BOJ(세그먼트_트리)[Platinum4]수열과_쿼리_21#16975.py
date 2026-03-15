import sys
input = sys.stdin.readline

def solve():
    n = int(input())
    a = [0] + list(map(int, input().split()))
    
    tree = [0] * (n + 2)

    def update(i, diff):
        while i <= n:
            tree[i] += diff
            i += (i & -i)

    def query(i):
        res = 0
        while i > 0:
            res += tree[i]
            i -= (i & -i)
        return res

    for i in range(1, n + 1):
        update(i, a[i] - a[i-1])

    m = int(input())
    ans = []
    
    for _ in range(m):
        query_data = list(map(int, input().split()))
        
        if query_data[0] == 1:
            _, i, j, k = query_data
            update(i, k)      
            update(j + 1, -k) 
        else:
            x = query_data[1]
            ans.append(str(query(x)))
    
    print('\n'.join(ans))
    
if __name__ == "__main__":
    solve()