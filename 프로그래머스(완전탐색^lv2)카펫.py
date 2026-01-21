def solution(brown, yellow):
    b_y_sum = brown + yellow
    
    # 가능한 모든 h 만들기
    curr = 3
    heights = []
    while True:
        if b_y_sum % curr == 0:
            heights.append(curr)
        if curr >= b_y_sum ** (1/2):
            break
        curr += 1
    
    # 하나면 굳이 안해봐도 유일한 해
    if len(heights) == 1:
        return (b_y_sum//heights[0], heights[0])

    for w, h in [(b_y_sum//h, h) for h in heights]:
        if yellow == (w - 2) * (h - 2):
            return([w, h])