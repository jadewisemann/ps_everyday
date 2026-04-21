from collections import deque


def solve():
    n, m = map(int, input().split())

    graph = [[] for _ in range(n + 1)]
    for _ in range(m):
        u, v = map(int, input().split())
        graph[u].append(v)
        graph[v].append(u)

    start, goal = map(int, input().split())

    visited_front = {start: None}
    visited_back = {goal: None}

    def bidirectional_bfs():
        q = deque([(start, "F"), (goal, "B")])
        while q:
            curr, direction = q.popleft()

            for neighbor in graph[curr]:
                if direction == "F":
                    if neighbor not in visited_front:
                        visited_front[neighbor] = curr
                        q.append((neighbor, "F"))

                        if neighbor in visited_back:
                            return neighbor

                else:  # direction == 'B'
                    if neighbor not in visited_back:
                        visited_back[neighbor] = curr
                        q.append((neighbor, "B"))

                        if neighbor in visited_front:
                            return neighbor

    meet_node = bidirectional_bfs()

    if not meet_node:
        return None

    def trace(curr, visited):
        path = []
        while curr is not None:
            path.append(curr)
            curr = visited[curr]
        return path

    return trace(meet_node, visited_front)[::-1] + trace(
        visited_back[meet_node], visited_back
    )


if __name__ == "__main__":
    print(solve())
