
def find_palindrome():
    n, m = map(int, input().split())
    strings = [input() for _ in range(n)]
    rotated_strings = ["".join(col) for col in zip(*strings)]
    ttl_strings = strings + rotated_strings

    for line in ttl_strings:
        for i in range(n - m + 1):
            sub =line[i : i + m]
            if sub == sub[::-1]:
                return sub
            
for tc in range(1, int(input()) + 1):
    print(f'#{tc} {find_palindrome()}')