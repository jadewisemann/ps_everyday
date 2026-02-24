MOD = 1000000007

n = int(input())

mul = lambda a, b: [
    [
        sum(x * y for x, y in zip(row, col)) % MOD
        for col in zip(*b)
    ]
    for row in a
]

res = [[1, 0], [0, 1]]
base = [[1, 1], [1, 0]]

while n > 0:
    if n % 2 == 1:
        res = mul(res, base)
    base = mul(base, base)
    n //= 2

print(res[0][1])    