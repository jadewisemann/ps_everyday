def recur_power(a, n, c):
    if n == 0:
        return 1
    
    half = recur_power(a, n // 2, c)
    
    if n % 2 == 0:
        return (half * half) % c
    else:
        return (half * half * a) % c

a, b, c = map(int, input().split())

print(recur_power(a % c, b, c))