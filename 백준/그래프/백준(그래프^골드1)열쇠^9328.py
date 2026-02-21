"""
백준.그래프.백준(그래프^골드1)열쇠^9328

사실 탐색 방법이,,,안중요해. 완탐이고
vis를 만들꺼야
그리고 돌면서 문을 만나면 => 확인해보고 => 없으면 => 저장
열쇠가 있으면 그냥 이동하고
만약 열쇠의 변동이 생긴다? 지금까지 만난 문을 전부 확인해보기
그러면 문은 dict여야 햐겠고 좌표를 가지고 있어야지
대소문자 구분이 되나?
`isupper()', 'islower()'가 있네
"""

"""
1 우선 패딩처리를 한다
2 ~~아무 지점~~ (0, 0)에서 순회를 시작한다. 
    => 패딩처리해서 .임이 보장되는 점이면 되겠지?
    => 0, 0에서 시작하자. 그러면 패딩을 친 .을 전부 돌면서 모든 집임점을 들어갈거야
    => bfs  해야 하네. dfs면 진입점 못 찾을 수도.
3 돌면서
    3a "#"을 만나면 cnt +1
    3b "."은 넘고, 벽은 안가고
    3c 키는 만나면
        키 목록에 넣고
        => 열 수 있는 문 있는지 확인하고 있으면 queue에 넣기
    3d 문은 키 확인
        => 있음? 열고 탐색 
        => 없음? 문: (좌표) 형태의 dict로 저장해 두기
"""

from collections import deque
import sys

input = sys.stdin.readline

# constant
DOCS = "$"
WALLS = "*"

for _ in range(int(input())):
    # 1. get inuput 
    h, w = map(int, input().split())

    # 1a. grid에 패딩 처리
    grid = [['.'] * (w + 2)]
    for _ in range(h):
        grid.append(['.'] + list(input().strip()) + ['.'])
    grid.append(['.'] * (w + 2))

    raw_keys = input().strip()
    keys = set()
    if raw_keys != 0:
        for key in raw_keys:
            keys.add(key)
    
    # 2. 순회
    vis = [[False for _ in range(w + 2)] for _ in range(h + 2)]
    doors = {}
    doc_counter = 0

    q = deque([(0, 0)])
    vis[0][0] = True

    while q:
        si, sj = q.popleft()

        # count 추가
        if grid[si][sj] == DOCS:
            doc_counter += 1

        # key를 발견
        curr = grid[si][sj]
        if curr.islower() and curr not in keys:
            keys.add(curr)
            if curr in doors:
                for ti, tj in doors[curr]:
                    q.append((ti, tj))
                    vis[ti][tj] = True            
    
                del doors[curr]
    
        # 4방향 순회
        for di, dj in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            ni, nj = si + di, sj + dj

            if not (0 <= ni < h + 2 and 0 <= nj < w + 2): continue
            if vis[ni][nj]: continue
            if grid[ni][nj] == WALLS: continue

            now = grid[ni][nj]
            if now.isupper() and now.lower() not in keys:
                doors.setdefault(now.lower(), []).append((ni, nj))
                continue

            q.append((ni, nj))
            vis[ni][nj] = True
            
    print(doc_counter)