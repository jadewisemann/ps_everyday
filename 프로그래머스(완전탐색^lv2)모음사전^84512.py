def solution(word):
    weights = [(31*5+1)*5 + 1, 31*5 + 1, 6*5 + 1, 5*1 + 1, 1]
    vowels = {'A': 0, 'E': 1, 'I': 2, 'O': 3, 'U': 4}
    answer = 0
    for i in range(len(word)):
        idx = vowels[word[i]]    
        answer += idx * weights[i] + 1
        
    return answer