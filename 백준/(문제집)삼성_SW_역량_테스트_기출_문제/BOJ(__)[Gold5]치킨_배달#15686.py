# gird[r < n][c < n]
# input_r: 1 - n
# input_c: 1 - n

# in grid
# > 0: empty
# > 1: house
# > 2: dinner
 
# "chicken distance" = 집에서 가장 가까운 치킨집 사이으 거리
# 각 집은 치킨거리가 있음
# 도시의 치킨 거리는 모든 집의 치킨 거리의 합

# M개만 남기고 치킨 집 폐업
# 즉 M개 선택


"""
완탐의 대상이 뭔가?
치킨 집
그러면 함수는 현재 cnt랑 치킨 집 인덱스 정도 가지고 있다가
매번 치킨 거리 계산
"""


"""
치킨 거리는 어캐 계산
치킨 집에서 bfs
그리고 더 작은 값으로 갱신
상태 복구 로직을 어캐 짜나?
"""

from collections import deque


def get_input():
    n, m = map(int, input().split())
    grid = [
        list(map(int, input()))
        for _ in range(n)
    ]
    return n, m, grid


def find_chicken_diner(n, grid):
    return [
        (r, c)
        for r in range(n)
        for c in range(n)
        if grid[r][c] == 2
    ]

def solve(n, m, grid, diner):
    dists = [[0] * n for _ in range(n)]

    min_chicken_number = float('inf')

    def get_min_chicken_number(curr_dinner_idx, dinner_cnt, curr_chicken_number):
        nonlocal min_chicken_number

        # 탐색 중단
        if dinner_cnt == m:
            if curr_chicken_number < min_chicken_number:
                min_chicken_number = curr_chicken_number
            return
        
        # 가지 치기
        if curr_chicken_number >= min_chicken_number: return
        
        
        # do bfs


        # update dist
        # send next state
        # restore dist


def main():
    n, m, grid  = get_input() 
    diners = find_chicken_diner(n, grid)
