
arr_1 = [1, 2, 3, 4, 5, 1, 2, 3, 4, 5]
arr_2 = [2, 1, 2, 3, 2, 4, 2, 5, 2, 1, 2, 3, 2, 4, 2, 5]
arr_3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5, 3, 3, 1, 1, 2, 2, 4, 4, 5, 5]

def solution(answers):
    scores = {
        1: 0,
        2: 0,
        3: 0
    }

    for idx in range(len(answers)):
        curr = answers[idx]
        if arr_1[idx%len(arr_1)] == curr:
            scores[1] += 1
        if arr_2[idx%len(arr_2)] == curr:
            scores[2] += 1
        if arr_3[idx%len(arr_3)] == curr:
            scores[3] += 1
    
    return([student for student, score in scores.items() if score == max(scores.values())])