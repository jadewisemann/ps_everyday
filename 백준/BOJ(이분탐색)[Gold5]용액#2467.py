n = int(input())
solutions = list(map(int, input().split()))
sorted_solutions = sorted(solutions)
l, r = 0, n - 1
res = None
gap = float('inf')
while l < r:
    concentration = sorted_solutions[r]  + sorted_solutions[l]
    
    if abs(concentration) < gap:
        gap = abs(concentration)
        res = (sorted_solutions[l], sorted_solutions[r])

    if concentration > 0:
        r -= 1
    elif concentration < 0:
        l += 1
    else:
        break

print(*res)