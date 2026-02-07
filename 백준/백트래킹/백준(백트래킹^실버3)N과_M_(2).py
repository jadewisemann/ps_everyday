n, m = map(int, input().split())


def a(start_number, number_arr):
    if len(number_arr) == m:
        print(" ".join(map(str, number_arr)))
        return 
    
    for idx in range(start_number, n + 1):
        a(idx + 1, number_arr + [idx])

a(1, []) 