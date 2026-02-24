fac = lambda n: n * fac(n-1) if n > 1 else 1

n, k = map(int, input().split())

print(fac(n) // (fac(k) * fac(n-k)))
