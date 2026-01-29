import heapq as hq

t = int(input())
for _ in range(t):
    m = int(input())
    arr = list(map(int, input().split()))

    mnh = []
    mxh = []

    for idx in range(m):
        if len(mnh) < len(mxh):
            hq.heappush(mnh, arr[idx])
        else:
            hq.heappush(mxh, -arr[idx]) 
        
        if mnh and mnh[0] < -mxh[0]:
            maxv = -hq.heappop(mxh)
            minv = hq.heappop(mnh)

            hq.heappush(mxh,  -minv)
            hq.heappush(mnh,  maxv)

        if idx % 2 == 0:
            print(-mxh[0], end=" ")
    print()


    