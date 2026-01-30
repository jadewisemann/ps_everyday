import heapq as hq

n = int(input())
arr = list(map(int, input().split()))

# Please write your code here.
hq.heapify(arr)
cnt = 0

for _ in range(n-1):
    a = hq.heappop(arr)
    b = hq.heappop(arr)
    cnt += a + b
    hq.heappush(arr, a + b)
    
print(cnt)

a, b = map(int, input().split())
a = list(map(int, input().split()))

iter(arr)
