for tc in range(int(input())):
    counts = [0] * 10
    n = int(input())
 
    for card in input():
        card = int(card)
        counts[card] += 1
 
    max_card, max_count = 0, 0
    for curr_card in range(1, 10):
        curr_count = counts[curr_card]
        if curr_count >= max_count:
            max_count = curr_count
            max_card = curr_card 
      
    print(f'#{tc + 1} {max_card} {max_count}')