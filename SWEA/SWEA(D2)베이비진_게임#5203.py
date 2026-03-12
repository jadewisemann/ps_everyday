for tc in range(int(input())):
    cards = list(map(int, input().split()))
    counts = [[0] * 12 for _ in range(2)] 
    winner = 0

    for i, v in enumerate(cards):
        p = i % 2 
        counts[p][v] += 1
        
        if (
            counts[p][v] == 3 or
            (counts[p][v] and counts[p][v+1] and counts[p][v+2]) or
            (counts[p][v-1] and counts[p][v] and counts[p][v+1]) or
            (counts[p][v-2] and counts[p][v-1] and counts[p][v])
        ):
            winner = p + 1
            break
            
    print(f"#{tc + 1} {winner}")