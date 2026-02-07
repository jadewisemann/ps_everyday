
# get input
n = int(input())
cards = list(map(int, (input().split())))

m = int(input())
m_arr = list(map(int, (input().split())))


# parse t dict
count_dict = {}
for card in cards:
    count_dict[card] = count_dict.get(card, 0) + 1

print(" ".join([str(count_dict.get(el, 0)) for el in m_arr]))
