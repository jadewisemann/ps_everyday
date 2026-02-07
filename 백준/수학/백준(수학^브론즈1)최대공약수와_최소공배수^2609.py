n, m = map(int, input().split())
l, s = (n, m) if n > m else (m, n)
gcd = 0

a, b = l, s
while True:
    remainder = a % b
    
    if remainder == 0:
        gcd = b
        break

    a, b = b, remainder

lcm = (l * s) // gcd

print(gcd)
print(lcm)