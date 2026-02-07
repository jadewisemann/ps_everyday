n, m = map(int, input().split())

def a(arr, start):
    if len(arr) >= m:
        print(' '.join(map(str, arr)))
        return

    for i in range(start, n + 1):
        a(arr + [i], i)

a([], 1)