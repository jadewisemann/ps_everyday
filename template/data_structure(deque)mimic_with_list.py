def inline_queue_operations():
    # [0] 초기 설정
    max_size = 10000
    q = [0] * max_size
    head = 0
    tail = 0

    # ----------------------------------------
    # [1] Push (오른쪽에 데이터 삽입)
    # 현재 tail 위치에 값을 넣고, tail을 1 증가시킵니다.
    # ----------------------------------------
    item_to_push = 10

    q[tail] = item_to_push
    tail += 1

    # ----------------------------------------
    # [2] Popleft (왼쪽에서 데이터 추출 - 일반적인 큐의 Pop)
    # 현재 head 위치의 값을 읽고, head를 1 증가시킵니다.
    # ----------------------------------------
    left_val = q[head]
    head += 1
    print(left_val)

    # ----------------------------------------
    # [3] Popright (오른쪽에서 데이터 추출 - 스택의 Pop)
    # tail을 먼저 1 감소시킨 후(마지막 요소 위치), 해당 값을 읽습니다.
    # ----------------------------------------
    tail -= 1
    right_val = q[tail]
    print(right_val)

    # ----------------------------------------
    # [4] Is Empty / Is Not Empty (상태 확인)
    # head와 tail 포인터가 같은 위치에 있다면 큐가 비어있는 상태입니다.
    # ----------------------------------------

    # 비어있는지 확인
    is_empty = head == tail

    # 비어있지 않은지 확인 (일반적인 while 루프 조건)
    is_not_empty = head < tail

    # 예시: 비어있지 않은 동안 반복
    while head < tail:
        val = q[head]
        head += 1
