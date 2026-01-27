def solution(progresses, speeds):
    n = len(progresses)
    days = [(100 - progresses[i]) // speeds[i] for i in range(n)]
    
    answer = []
    return answer