# class Queue:
#     def __init__(self):
#         self.queue = list()
#         def addto(self,dataval):
#             if dataval not in self.queue:
#                 self.queue.insert(0, dataval)
#             return True
#         return False
#     def size(self):
#         return len(self.queue)
    
#     TheQueue = Queue()

#     TheQueue.addto("Mon")

#     TheQueue.addto("Tue")

#     TheQueue.addto("Wed")

#     print(TheQueue.size())

queue = []

# adding elements
queue.append("a")
queue.append("b")
queue.append("c")
queue.append("c")

print("Initial queue: ", queue)


queue = []

# adding elements
queue.append("a")
queue.append("b")
queue.append("c")
queue.append("d")

print("Initial queue")
print(queue)
print("\nElements dequeued from queue")

# removing elements
print(queue.pop(0))
print(queue.pop(0))
print(queue.pop(0))
print("queue after removing elements")
print(queue)