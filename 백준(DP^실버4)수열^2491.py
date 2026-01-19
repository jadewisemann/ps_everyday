n = int(input())
arr  = list(map(int, input().split()))


asc = 1
asc_his = []
des = 1
des_his = []

pre = 0

for num in arr:
    if not pre:
        pre = num
        continue

    if pre < num:
        asc += 1
        des_his.append(des)
        des = 1
    elif pre > num:
        des += 1
        asc_his.append(asc)
        asc = 1
    else:
        des += 1
        asc += 1

    pre = num
    
print(max(max(des_his), max(asc_his)))
