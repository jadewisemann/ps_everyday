for tc in range(int(input())):
    n = int(input())
    arr = input().split()

    mid = (n - 1)//2 + 1
    res = [None] * n 
    res[::2], res[1::2] = arr[:mid], arr[mid:]

    print(f'#{tc + 1}', *res)
    