mapper = {
    "+": 1,
    "*": 2,
}

for tc in range(10):
    n = int(input()) 
    rear_calc = ""
    stck = []

    for char in input():
        if char.isdigit():
            rear_calc += char
        else:
            while stck and mapper[stck[-1]] >= mapper[char]:
                rear_calc += stck.pop()
            
            stck.append(char)

    while stck:
        rear_calc += stck.pop()
    
    calc_stck =  []

    for char in rear_calc:
        if char.isdigit():
            calc_stck.append(int(char))
        else:
            b, a = calc_stck.pop(), calc_stck.pop()
            calc_stck.append(
                a + b if char == "+" else
                a * b
            )
    
    print(f'#{tc + 1} {calc_stck[0]}')
