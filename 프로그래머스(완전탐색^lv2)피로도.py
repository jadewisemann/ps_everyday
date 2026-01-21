def solution(k, dungeons):
    n = len(dungeons)
    
    # step 1. 가능한 모든  조합 만들기
    arr = [[i] for i in range(n)]
    p_dungeons = []
    
    while arr:
        curr = arr.pop()
        
        if len(curr) >= n:
            p_dungeons.append(curr)
            continue
        
        for i in range(n):
            if i in curr:
                continue

            arr.append(curr + [i])

    counts = []
    
    for p_dungeon in p_dungeons:
        tmp_k = k
        tmp_count = 0
        for index in p_dungeon:
            need, consume = dungeons[index]
            if tmp_k < need:
                counts.append(tmp_count)
                break
            tmp_k -= consume
            tmp_count += 1
        counts.append(tmp_count)

    return(max(counts))