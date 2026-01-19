# 10 2
# 3 -2 -4 -9 0 3 7 13 8 -3

# 초기 인풋
n, k = map(int, input().split())
arr = list(map(int, input().split()))

# 초기 변수

fi = 0
bi = k - 1
win = sum(arr[0:k])
tmp = [win]

# 루프
while True:
    # 예외 조건
    if k == 1: break


    # 순차 진행
    fi += 1
    bi += 1

    # 종료 조건
    if bi >= n: break
    
    win = win - arr[fi-1] + arr[bi]


    tmp.append(win)
    

print(max(arr if k == 1 else tmp))