def tournament(i, j, cards):
    if i == j:
       return i
    
    m = (i + j) // 2
    l, r = tournament(i, m, cards), tournament(m + 1, j, cards)
    
    return r if (cards[l] - cards[r]) % 3 == 2 else l

for tc in range(int(input())):
    print(f"#{tc + 1} {tournament(1, int(input()), [0] + list(map(int, input().split())))}")