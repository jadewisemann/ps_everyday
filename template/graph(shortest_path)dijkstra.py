import heapq

INF = float('inf')

vertex, edgte = map(int, input().split())
start = int(input())

grp = [[] for _ in range(vertex + 1)]
dists = [INF] * (vertex + 1)

for _ in range(edgte):
    u, v, w = map(int, input().split())
    grp[u].append((v, w))

# 초기값
min_heap = []
heapq.heappush(min_heap, (0, start))
dists[start] = 0

# 최소힙에서 계속 거리가 최소인 정점_vertex_ 추출하면서 거리 갱신
while min_heap:
    dist_till_curr, curr = heapq.heappop(min_heap)
    
    # 만약 현재까지의 거리가 저장된 거리보다 크다? 필요 없는 경로, 최단 경로는 아님
    if dist_till_curr > dists[curr]:
        continue

    for neigbor, weight in grp[curr]:
        dist_to_neighbor = dist_till_curr  + weight

        # 이웃까지의 거리가 저장된 거리보다 길면? 최단 경로 아님
        if dist_to_neighbor >= dists[neigbor]:
            continue

        dists[neigbor] = dist_to_neighbor
        # 최소 힙안에 있는 값은 수정하는 것이 아니라 갱신된 값을 넣어서 지연 삭제
        heapq.heappush(min_heap, (dist_to_neighbor, neigbor))
