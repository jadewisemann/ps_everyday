from collections import Counter

n, m, b = map(int, input().split())
counter = Counter(int(x) for _ in range(n) for x in input().split())

ans_time, ans_height = float('inf'), 0
    
for goal_h in range(257):
    added, removed = 0, 0
    
    for h, count in counter.items():  
        if h > goal_h:
            removed += (h - goal_h) * count
        elif h < goal_h:
            added += (goal_h - h) * count
         
    if removed + b >= added:
        time = removed * 2 + added
        if time <= ans_time:
            ans_time, ans_height = time, goal_h
            
print(ans_time, ans_height)