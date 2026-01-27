def solution(N, stages):
    passed = [0] * (N+1)
    fail = [0] * (N+1)

    for i in range(N):
        curr = i + 1
        for stage in stages:
            if stage > curr:
                passed[curr] += 1
            elif stage == curr:
                fail[curr] += 1
    
    failure_ratio = []

    for i in range(N):
        curr = i+1
        failure_ratio.append([curr, fail[curr]/ (passed[curr] + fail[curr]) if fail[curr] else 0])

    
    answer = [i for i, _ in sorted(failure_ratio, key= lambda x: -x[1])]
    return answer