import heapq

INF = float('inf') 

def dijkstra(number_of_vertex, start, graph):
    # 거리, inf로 초기화, 시작점은 0
    dist = [INF] * (number_of_vertex + 1)
    parent = [0] * (number_of_vertex + 1)

    dist[start] = 0
    pq = [(0, start)]

    while pq:
        dist__start_to_current, current_vertex = heapq.heappop(pq)
        
        # distance에 저장된 현재 정점(current_vertex)까지의 거리보다 길다? 넘어감
        if dist__start_to_current > dist[current_vertex]: continue
        
        # 파싱한 그래프에서 다음 정점과 그 거리를 추출
        for next_vertex, distance__current_to_next in graph[current_vertex]:
            dist__start_to_next = dist__start_to_current  + distance__current_to_next

            # 이웃까지의 거리가 저장된 거리보다 길면? 최단 경로 아님
            if dist__start_to_next >= dist[next_vertex]: continue

            dist[next_vertex] = dist__start_to_next
            # 누가 날 업데이트 했는지 기록, 어디서 연결했는지 기록
            parent[next_vertex] = current_vertex

            # 최소 힙안에 있는 값은 수정하는 것이 아니라 갱신된 값을 넣어서 지연 삭제
            heapq.heappush(pq, (dist__start_to_next, next_vertex))

    return dist, parent

def traceback(parents, start, end):
    path = []
    curr = end
    
    while curr != start:
        path.append(curr)
        curr = parents[curr]
    
    path.append(start)
    return path[::-1]


def main():
    # get input
    number_of_vertex, number_of_edge = map(int, input().split())
    start = int(input())
    end = int(input())
    
    # graph parsing
    graph = [[] for _ in range(number_of_vertex + 1)]
    for _ in range(number_of_edge):
        u, v, w = map(int, input().split())
        graph[u].append((v, w))
 
    # dijkstra, 역추적 call
    dist, parent = dijkstra(number_of_vertex, start, graph)        
    path = traceback(parent, end, start)

    # 출력
    print(*dist)
    print(*path)

if __name__ == "__main__":
    main()