import heapq as hq

iterator = iter(open(0).read().split())

n = int(next(iterator))

mxh, mnh, rst = [], [], []

for el in iterator:
    el = int(el)
    
    if len(mxh) == len(mnh):
        hq.heappush(mxh, -hq.heappushpop(mnh, el))
    else:
        hq.heappush(mnh, -hq.heappushpop(mxh, -el))

    rst.append(str(-mxh[0]))

print('\n'.join(rst))