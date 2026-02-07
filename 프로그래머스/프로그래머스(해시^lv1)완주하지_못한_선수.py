def solution(participants, completions):
    dict = {}
    for p in participants:
        dict[p] = dict.get(p, 0) + 1
    
    for c in completions:
        dict[c] -= 1
    
    for key, value in dict.items():
        if value > 0:
            return key
        

from collections import Counter

def solution_2(participants, completions):
    ans = Counter(participants) - Counter(completions)

    return list(ans.keys())[0]

def solution_3(participants, completions):
    tmp = 0
    dict = {}
    
    for p in participants:
        h = hash(p)
        dict[h] = p
        temp += h

    for c in completions:
        temp -= hash(c)
    
    return dict[tmp]


