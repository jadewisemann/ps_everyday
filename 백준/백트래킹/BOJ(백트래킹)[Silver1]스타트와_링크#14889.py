from itertools import combinations

def solve():
    n = int(input())
    table = [
        list(map(int, input().split()))
        for _ in range(n)
    ]

    row_sums = [sum(row) for row in table]
    col_sums = [sum(col) for col in zip(*table)]
    
    player_score = [r + c for r, c in zip(row_sums, col_sums)]
    
    total_val = sum(row_sums) 

    min_diff = float('inf')
    nums = list(range(n))

    for comb in combinations(nums[1:], n // 2 - 1):
        strt_score = player_score[0] + sum(player_score[i] for i in comb)

        diff = abs(total_val - strt_score)

        if diff < min_diff:
            min_diff = diff

        if min_diff == 0: break

    print(min_diff)

solve()