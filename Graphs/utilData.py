# Data Structure Utilities
# John Andrew Taylor, 2019
# General purpose classes defining data structures.
# Included are Stack, Queue, and PriorityQueue
#

import heapq

class Stack:
    def __init__(self):
        self.stack = []

    def push(self,a):
        self.stack.append(a)

    def pop(self):
        return self.stack.pop()

    def isEmpty(self):
        return not self.stack

class Queue:
    def __init__(self):
        self.queue = []

    def push(self,a):
        self.queue.insert(0,a)

    def pop(self):
        return self.queue.pop()

    def isEmpty(self):
        return not self.queue

class PriorityQueue:
    def  __init__(self):
        self.pq = []

    def push(self, a, order):
        heapq.heappush(self.pq, (order, a))

    def pop(self):
        _, a = heapq.heappop(self.pq)
        return a

    def isEmpty(self):
        return not self.pq
