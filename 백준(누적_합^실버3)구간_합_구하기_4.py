ip = lambda: map(int, input().split())

n, m = ip()
narr = list(ip())
marr = [list(ip()) for _ in range(m)]

prefix = [narr[0]]

for i in range(1, n):
    prefix.append(prefix[i-1] + narr[i])
prefix = [0] + prefix


for l, r in marr:    
    print(prefix[r] - prefix[l-1])