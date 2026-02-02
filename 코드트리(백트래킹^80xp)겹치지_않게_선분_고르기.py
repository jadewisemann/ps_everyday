n = int(input())
x1, x2 = [], []

for _ in range(n):
    a, b = map(int, input().split())
    x1.append(a)
    x2.append(b)

# Please write your code here.


candi = [i for i in range(n)]

cnts = []

def sel(curr, points):
    # points
    
    # base
    len_curr = len(curr)
    if len_curr >= n:
        cnts.append(len_curr)
        return
    
    for el in candi:
        if el not in points:
            sel([*curr, el])  

sel([[el] for el in candi])

print(max(cnts))