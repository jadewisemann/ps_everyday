fibo = [[0, 1], [1, 0]]
for _ in range(int(input())):
    n = int(input())
    if n >= len(fibo):
        for curr in range(2, n+1):
            a, b = fibo[-1]
            c, d = fibo[-2]
            fibo.append([a + b, c + d])

    a, b = fibo[n]
    print(b, a)