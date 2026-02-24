N = int(input())
grp = [list(map(int, input().split())) for _ in range(N)]
max_arr = [*grp[0]]
max_temp = [*grp[0]]
for i in range(1,N):
    max_temp = [grp[i][0]+min(max_arr[1],max_arr[2]), grp[i][1] + min(max_arr[0], max_arr[2]),grp[i][2]+min(max_arr[0], max_arr[1]),]
    max_arr = max_temp; max_temp = [0,0,0]
print(min(max_arr))