from collections import deque


class FIFOQueue():
    def __init__(self):
        self.__dequeue = deque()


    def is_empty(self):
        return len(self.__dequeue) == 0
    

    def pop(self):
        if not self.is_empty():
            return self.__dequeue.popleft()
        else:
            raise IndexError("Pop from an empty queue")
    

    def top(self) -> 'any':
        if not self.is_empty():
            return self.__dequeue[0]
        else:
            raise IndexError("Top from an empty queue")
        

    def add(self, node: 'any'):
        self.__dequeue.append(node)


    def size(self) -> 'int':
        return len(self.__dequeue)