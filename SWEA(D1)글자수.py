for tc in range(1, int(input()) + 1):
    a_str = input()
    b_str = input()
    max_val = 0
    for a_char in a_str:
        char_sum = 0
        for b_char in b_str:
            if b_char == a_char:
                char_sum += 1
        
        if char_sum > max_val:
            max_val = char_sum

    print(f'#{tc} {max_val}')