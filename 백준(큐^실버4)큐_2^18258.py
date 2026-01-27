from collections import deque

tokens = iter(open(0).read().split())

n = next(tokens)

queue = deque([])
results = []

for cmd in tokens:
    if cmd == "push":
        value = next(tokens)
        queue.append(value)
    
    elif cmd == "pop":
        results.append(queue.popleft() if queue else -1)
        
    elif cmd == "size":
        results.append(len(queue))

    elif cmd == "empty":
        results.append(0 if queue else 1)

    elif cmd == "front":
        results.append(queue[0] if queue else -1)

    elif cmd == "back":
        results.append(queue[-1] if queue else -1)

    
print("\n".join(map(str, results)))
