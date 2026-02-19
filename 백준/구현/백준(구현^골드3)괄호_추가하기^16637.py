def calculate(a, b, op):
    if op == '+':
        return a + b
    elif op == '-':
        return a - b
    elif op == '*':
        return a * b

def dfs(idx, curr_val):
    global ans

    # base condition 
    if idx == len(ops):
        ans = max(ans, curr_val)
        return

    res1 = calculate(curr_val, nums[idx + 1], ops[idx])
    dfs(idx + 1, res1)

    if idx + 1 < len(ops):
        bracket_val = calculate(nums[idx + 1], nums[idx + 2], ops[idx + 1])
        res2 = calculate(curr_val, bracket_val, ops[idx])
        dfs(idx + 2, res2)


n = int(input())
expression = input()

nums, ops = [], []
for i in range(n):
    if i % 2 == 0:
        nums.append(int(expression[i]))
    else:
        ops.append(expression[i])

ans = -float('inf')

dfs(0, nums[0])
    
print(ans)
