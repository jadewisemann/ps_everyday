n = int(input())
arr = list(map(int, input().split()))

count = [0] * 10
max_lenght, l, r, kind = 0, 0, 0, 0

for _ in range(n):
    right_fruit = arr[r]

    if count[right_fruit] == 0:
        kind += 1
    count[right_fruit] += 1

    while kind > 2:
        left_fruit = arr[l]
        count[left_fruit] -= 1
        if count[left_fruit] == 0:
            kind -= 1
        l += 1

    curr_length = r - l + 1
    if curr_length > max_lenght:
        max_lenght = curr_length

    r += 1

print(max_lenght)