n = int(input())
arr = list(map(int, input().split()))

# Please write your code here.
import heapq as hq

rst = []
mnh = [(el, i) for i, el in enumerate(arr)]
dels = [False] *n
tsum = sum(arr)
count = n
hq.heapify(mnh)

for k in range(n-3):
    tsum -= arr[k]
    count -= 1
    dels[k] = True

    while mnh and dels[mnh[0][1]]:
        hq.heappop(mnh)

    if mnh:
        minv = mnh[0][0]
        rst.append((tsum - minv) / (count - 1))

if rst:
    print(f'{max(rst):.2f}')