from queue import PriorityQueue

customers = PriorityQueue()
customers.put((2, "Harry"))
customers.put((3, "Charles"))
customers.put((1, "Riya"))
customers.put((4, "Stacy"))

while customers.qsize() != 0:
    print(customers.get())

import heapq

employees = [21,1,45,78,3,5]
heapq.heapify(employees)
heapq.heappush(employees, 4)
heapq.heappush(employees, 2)
while employees:
    print(heapq.heappop(employees))
