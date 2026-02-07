def solution(progresses, speeds):
    n = len(progresses)
    days = [(100 - progresses[i]) // speeds[i] for i in range(n)]
    #  7, 3, 9
    stk = []
    while stk:
        
        curr = stk.pop()
        
    # 5, 10, 1, 1, 20 ,1
    answer = []
    return answer