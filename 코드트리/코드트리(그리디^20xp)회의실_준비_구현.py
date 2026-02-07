n = int(input())
meetings = [tuple(map(int, input().split())) for _ in range(n)]

# Please write your code here.
meetings.sort(key= lambda x: x[1])

cnt = 0
end = 0

for meeting in meetings:
    s, e = meeting
    if s >= end:
        cnt += 1
        end = e
        
print(cnt)