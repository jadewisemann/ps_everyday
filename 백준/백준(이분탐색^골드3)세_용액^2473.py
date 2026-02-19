import sys
input = sys.stdin.readline

n = int(input())
solutions = list(map(int, input().split()))

sorted_solution = sorted(solutions)

a, b, c = 0, 0, 0
close_sum = float('inf')

exit_flag = False

for i in range(n - 2):
    if exit_flag:
        break    

    l, r = i + 1, n - 1

    while l < r:
        curr_sum = (
            sorted_solution[i] + sorted_solution[l] + sorted_solution[r]
        )
        abs_sum = abs(curr_sum)

        if abs_sum < close_sum:
            close_sum = abs_sum
            a, b, c = sorted_solution[i], sorted_solution[l], sorted_solution[r]

        if curr_sum < 0:
            l += 1
        elif curr_sum > 0:
            r -= 1
        else:
            exit_flag = True
            break

print(a, b, c)
