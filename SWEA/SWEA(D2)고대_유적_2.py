for tc in range(1, int(input()) + 1):
    n, m = map(int, input().split())
    grid = [input().replace(' ', '') for _ in range(n)]
    
    invert = [''.join(row) for row in zip(*grid)]
    
    max_len = 0

    for line in grid + invert:
        lengths = [len(ones) for ones in line.split('0') if len(ones) >= 2]
        if lengths:
            max_len = max(max_len, max(lengths))
            
    print(f'#{tc} {max_len}')