import heapq

H = [21,1,45,78,3,5]
heapq.heapify(H)
print(H)

heapq.heappush(H,8)
print(H)

heapq.heappop(H)
print(H)

heapq.heapreplace(H,6)
print(H)