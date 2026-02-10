memo = {
    1: 1,
    2: 3,
}

def square(n):
    if n not in memo:
        memo[n] = square(n - 1) + square(n - 2) * 2
    return memo[n]

for tc in range(int(input())):
    print(f'#{tc + 1} {square(int(input()) // 10)}') 