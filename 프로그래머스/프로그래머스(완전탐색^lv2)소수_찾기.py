def is_prime(num):
    if num == 0 or num == 1 : return False
    for i in range(2,num):
        if num % i == 0:  
            return False
    return True

def solution(numbers):
    # step 1: 입력받기
    n = len(numbers)
    # 리스트로 변환
    numbers = list(numbers)
        # str: 시퀀셜한 이터러블한 객체
            # 따라서 list로 형변환시 각 문자가 list에 하나씩 담김
            # 즉 자동으로 분해됨 
        # "123" => ['1', '2', '3']

    # step 2: 숫자 모두 만들기
    # <Main Idea> 인덱스만 넣기 
        # 왜? 
        # 문자로만 관리하면 쉽지만, 하나의 리스트에 문자가 여러개인 경우가 있음
        # 따라서 문자는 유일한 값이 아님
        # 그래서 유일한 값인 인덱스를 관리
    
    # 결과 저장 리스트는 셋으로.
        # 왜? 중복허용하지 않는 자료형
        # 리스트와 달리 비어있는 set은 신테틱 슈거로 못 만듬
            # 집합: `{'1', '2', '3', ...}`
            # {}는 비어있는 집합이 아니라 비어있는 딕셔너리를 만듬
    rst = set()
    
    # 순회, loop
    # 초기값 넣어주기
    arr = []
    for i in range(n):
        arr.append(i)
    
    # 리스트 컴프리헨션으로 축약 가능
    # arr = [[i] for i in range(n)] 
    
    while arr:
        # 모든 pop한것을 담는게 핵심
        curr = arr.pop()

        # 인덱스를 숫자에 대응시켜서 set에 넣기
            # 굳이?
            # set은 해셔블한 값만 원소로 받을 수 있음
            # list는 가변하므로 헤셔블 하지 않아서 set의 원소가 되지 못함
        num = int("".join(numbers[i] for i in curr))
        rst.add(num)

        # n보다만 작으면
        if len(curr) < n:
            # 모든 원소를 이어 붙임
            for i in range(n):
                # 단 이미 있는 것만 빼고
                if i not in curr:
                    arr.append(curr + [i])
    
    
    # 소수 판별
    counter = 0
    for num in rst:
        if is_prime(num):
            counter += 1
    
    return counter
