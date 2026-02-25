from collections import deque

cards = deque([i + 1 for i  in range(int(input()))])

while len(cards) > 1:
    cards.popleft()
    cards.rotate(-1)

print(cards[0])