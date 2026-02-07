result_count, round_bracket_count, squre_bracket_count = 0, 0, 0
stk = []
is_closed = False
flag = False
for chr in input():
    if chr == "(":
        stk.append(chr)
        round_bracket_count += 1
        is_closed = False
    elif chr == "[":
        stk.append(chr)
        squre_bracket_count += 1
        is_closed = False
    elif chr == ")":
        if not stk or stk[-1] != "(":
            flag = True
            break  
        stk.pop()
        round_bracket_count -= 1
        if not is_closed:
            result_count += 2 * 2 ** round_bracket_count * 3 **squre_bracket_count
            is_closed = True
    elif chr == "]":
        if not stk or stk[-1] != "[":
            flag = True
            break  
        stk.pop()
        squre_bracket_count -= 1
        if not is_closed:
            result_count += 3 * 2 ** round_bracket_count * 3 **squre_bracket_count
            is_closed = True

print(result_count if not flag and not stk else 0)
