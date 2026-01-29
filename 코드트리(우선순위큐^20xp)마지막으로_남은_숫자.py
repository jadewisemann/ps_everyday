n = int(input())
arr = list(map(int, input().split()))

# Please write your code here.
import heapq as hq
# 가장 큰 수 2개
# 두 수의 diff 삽입
# 제약. 2개의 수가 배열에
# 0이면 안넣음
#마지막으로 남은 수 출력


mxh = [-i for i in arr]
hq.heapify(mxh)

while len(mxh) >= 2:  
    a = -hq.heappop(mxh)
    b = -hq.heappop(mxh)
    diff  = a - b
    hq.heappush(mxh, -diff)

ans = -hq.heappop(mxh)
print(ans)