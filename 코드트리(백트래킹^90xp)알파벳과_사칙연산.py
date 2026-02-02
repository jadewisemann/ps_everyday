expression = input()

# Please write your code here.
ops = []
char_cnt = 0

for char in expression:
    if char in "abcdef":
        char_cnt += 1 
    else:
        ops.append(char)

max_val = 0

def a(idx, nums):
    if idx == char_cnt:
            
        # 계산
        # max

        return 
    
    for num in [1, 2, 3, 4]:
        a(idx + 1, [*nums, num])    

a(0, [])


    
