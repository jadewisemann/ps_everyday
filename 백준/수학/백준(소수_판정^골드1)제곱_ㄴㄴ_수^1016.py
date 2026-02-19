min_range, max_range = map(int, input().split())

is_sq_nn = [True] * (max_range - min_range + 1)

for i in range(2, int(max_range ** 0.5) + 1):
    square = i * i

    curr = (min_range // square) * square
    if curr < min_range:
        curr += square

    for j in range(curr, max_range + 1, square):
        is_sq_nn[j - min_range] = False

print(is_sq_nn.count(True))
