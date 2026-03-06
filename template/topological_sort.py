from collections import deque

def get_paresed_data():
    n, m = map(int, input().split())
    # n + 1 만큼 인접 관계 배열 미리 선언 => dict도 괜찮은데 이게 더 빠름
    adjacency = [[] for _ in range(n + 1)]
    # 진입 차수 배열도 미리 선언
    indegree = [0] * (n + 1)

    for _ in range(m):
        # 위상정렬은 가중치가 중요하지 않고 어디서 어디로 이어지는지만 필요함
        start, end = map(int, input().split())
        # 시작점의 인접 관계에 끝점 추가
        adjacency[start].append(end)
        # "끝점"의 진입 차수에 1 추가(시작점)
        indegree[end] += 1

    return n, adjacency, indegree


def topological_sort(n, adjs, indegree):        
    # 큐에 진입차수가 0인 정점만 넣기
    queue = deque([])
    for i in range(1, n + 1):
        if indegree[i] == 0:
            queue.append(i)

    result = []
    # 진입 차수가 0인 정점만 뽑으면서 순회하기
    while queue:
        # now: 진입 차수가 0인 정점
        now = queue.popleft()   
        # 결과에 바로 넣어주기
        result.append(now)
        # 진입차수가 0인 정점에 연결된(인접한) 점들에 대해
        for nxt in adjs[now]:
            # 진입 차수 1을 빼줌
            indegree[nxt] -= 1
            # 만약 그래서 진입차수가 0이 되었다면
            if indegree[nxt] == 0:
                # 다시 큐에 넣기
                queue.append(nxt)
    
    return result

def main():
    # adjagcency = 인접
    # indegree = 진입 차수
    n, adjacency, indegree = get_paresed_data()
    result = topological_sort(n, adjacency, indegree)
    print(*result)

if __name__ == "__main__":
    main()


