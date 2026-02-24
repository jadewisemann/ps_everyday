from collections import deque

n, k = map(int, input().split())
rst =  []
dq = deque([str(i +1) for i in range(n)])

for _ in range(n):
    dq.rotate(-k)
    a = dq.pop()
    rst.append(a)


print(f'<{", ".join(rst)}>')