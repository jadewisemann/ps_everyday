#  일반적인 dfs 풀이

def solution(numbers, target):
    # 초기 인풋
    init_number = numbers[0]
    n = len(numbers)
    count = 0
    
    # 루프
    stack = [[init_number, 0], [(-1) * init_number, 0]]
    while stack:
        number, idx = stack.pop()
        
        # 종료 조건
        if idx == n:
            # 결과 기록
            if number == target:
                count += 1
            continue
        
        # 제약 조건 => 없음

        # stack에 추가
        n_idx =  idx + 1
        d_number = numbers[n_idx]
        stack += [[number + d_number, n_idx], [number - d_number, n_idx]]
# 

    answer = count 
    return answer
