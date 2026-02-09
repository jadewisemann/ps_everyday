n = int(input())
points = [tuple(map(int, input().split())) for _ in range(n)]

area = 0
for i in range(n):
    j = (i + 1) % n
    area += points[i][0] * points[j][1]
    area -= points[j][0] * points[i][1]

print(round(abs(area)/2, 2))