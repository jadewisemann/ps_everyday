def heap_push(value):
    heap.append(value)
    curr = len(heap) - 1
    while curr > 1:
        parent = curr // 2
        if heap[curr] < heap[parent]:
            heap[curr], heap[parent] = heap[parent], heap[curr]
            curr = parent
        else:
            break


for tc in range(int(input())):
    n = int(input())
    nums = list(map(int, input().split()))
    
    heap = [0]
    for num in nums:
        heap_push(num)
    
    total = 0
    idx = n // 2
    while idx > 0:
        total += heap[idx]
        idx //= 2
        
    print(f"#{tc + 1} {total}")