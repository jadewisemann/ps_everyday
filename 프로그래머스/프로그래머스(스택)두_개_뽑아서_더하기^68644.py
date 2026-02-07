def solution(numbers):
    tmp = []
    n = len(numbers)
    for i in range(n):
        for j in range(i+1, n):
            tmp.append(numbers[i] + numbers[j])
    return sorted(list(set(tmp)))