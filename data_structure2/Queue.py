

class Queue:
    MAX = 10

    def __init__(self):
        self.queue = [None] * self.MAX
        self.front, self.rear, self._size = 0, 0, 0

    def enqueue(self, data):
        if not self.is_full():
            self.queue[self.front] = data
            self.front = self.next(self.front)
            self._size += 1

    def dequeue(self):
        if not self.is_empty():
            data = self.queue[self.rear]
            self.rear = self.next(self.rear)
            self._size -= 1
            return data
        else:
            return None

    def is_empty(self):
        return self.rear == self.front

    def is_full(self):
        return self.next(self.front) == self.rear

    def size(self):
        return self._size

    def next(self, index):
        return (index + 1) % self.MAX

    def print(self):
        pass

