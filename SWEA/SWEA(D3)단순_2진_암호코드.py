mapper = {
    '0001101': 0,
    '0011001': 1,
    '0010011': 2, 
    '0111101': 3,
    '0100011': 4,
    '0110001': 5,
    '0101111': 6,
    '0111011': 7,
    '0110111': 8, 
    '0001011': 9
}

mapping = lambda x: mapper[x]

for tc in range(int(input())):
    n, m = map(int, input().split())
    
    target = ""
    for _ in range(n):
        row = input()
        if not target and '1' in row:
            target = row
    
    last_idx = 0
    for i in range(m - 1, -1, -1):
        if target[i] == '1':
            last_idx = i
            break
            
    first_idx = last_idx - 55
    
    code_part = target[first_idx : last_idx + 1]
    
    decoded = [
        mapping(code_part[i * 7 : (i + 1) * 7])
        for i in range(8)
    ]
    
    odd_sum = sum(decoded[i] for i in range(8) if i % 2 == 0)
    even_sum = sum(decoded[i] for i in range(8) if i % 2 == 1)
    
    verification = (odd_sum * 3) + even_sum
    
    print(f"#{tc + 1}", end=" ")
    if verification % 10 == 0:
        print(sum(decoded))
    else:
        print(0)