ip = lambda: map(int, input().split())

n, m = ip()
narr = list(ip())

prefix = [0] * (n+1)

sum = 0
for i in range(n):
    sum += narr[i]
    prefix[i+1] = sum

output = []
for _ in range(m):
    l, r = ip()    
    output.append(str(prefix[r] - prefix[l-1]))

print("\n".join(output))