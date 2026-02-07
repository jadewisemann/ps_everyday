n = int(input())
x1, x2 = [], []

for _ in range(n):
    a, b = map(int, input().split())
    x1.append(a)
    x2.append(b)

# Please write your code here.
def sel(curr, idx):

    if idx >= n:
        return len(curr)

    f = True
    for sidx in curr:
        if not  (x2[idx]  < x1[sidx] or  x2[sidx] < x1[idx]):
            f = False
            break
    
    rst = 0
    if f:
        curr.append(idx)
        rst = sel(curr, idx + 1)
        curr.pop()

    return max(rst, sel(curr, idx + 1))

print(sel([], 0))
