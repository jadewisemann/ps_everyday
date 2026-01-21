def solution(word):
    vowels = 'UOIEA'
    stack = ['']
    count = -1

    while stack:
        curr = stack.pop()
        count += 1
        
        if curr == word:
            return count
        
        if len(curr) < 5:
            for v in vowels:
                stack.append(curr + v)

def solution_2(word):
    weights = [(31*5+1)*5 + 1, 31*5 + 1, 6*5 + 1, 5*1 + 1, 1]
    vowels = {'A': 0, 'E': 1, 'I': 2, 'O': 3, 'U': 4}
    answer = 0
    for i in range(len(word)):
        idx = vowels[word[i]]    
        answer += idx * weights[i] + 1
        
    return answer