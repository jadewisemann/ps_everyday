expression = input()

# Please write your code here.
ops = []


chars = []

for char in expression:
    if char in "abcdef":
        chars.append(char)
    else:
        ops.append(char)

max_val = 0

len_char = len(set(chars))

def a(idx, nums):
    if idx == len_char:    
        # 계산
        prev = chars[0]
        for i in range(1,len(chars)):
            curr_ops = ops[i - 1]
            curr_nums = chars
            if curr_ops == '+':
                prev =
        # max
        return
    
    for num in [1, 2, 3, 4]:
        a(idx + 1, [*nums, num])    


a(0, [])


    
