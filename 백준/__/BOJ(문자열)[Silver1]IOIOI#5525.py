n, m, string = int(input()), int(input()), input()  

res, i, cnt = 0, 1, 0

while i < (m - 1):
    if string[i - 1] == 'I' and string[i] == 'O' and string[i + 1] == 'I':
        cnt += 1

        if cnt >= n:
            res += 1

        i += 2
    else:
        cnt = 0
        i += 1

print(res)