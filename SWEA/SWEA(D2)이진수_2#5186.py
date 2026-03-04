for tc in range(int(input())):
    n      = float(input())
    result = ""
    cnt    = 0

    while n > 0:
        n   *= 2
        cnt += 1

        if cnt >= 13: 
            result = "overflow"
            break

        if n >= 1:
            result += "1"
            n -= 1
        else:
            result += "0"

    print(f'#{tc + 1} {result}')