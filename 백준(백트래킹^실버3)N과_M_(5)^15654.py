ip = lambda: map(int, input().split())

n, m = ip() 
numbers = sorted(list(ip()))

def a(num_arr):
    if len(num_arr) >= m:
        print(" ".join(map(str, num_arr)))
        return
    
    for num in numbers:
        if num in num_arr:
            continue
        a(num_arr + [num])

a([])