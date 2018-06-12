
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self._size = 0

    def append(self, data):
        node = Node(data)
        if self.head is None:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            self.tail = node
        self._size += 1

    def search(self, data):
        cur = self.head
        while cur:
            if cur.data == data:
                return cur
            cur = cur.next
        return None

    def remove(self, data):
        prev, cur = None, self.head
        while cur:
            if cur.data == data:
                if cur == self.head:
                    self.head = cur.next
                else:
                    prev.next = cur.next
                self._size -= 1
            prev = cur
            cur = cur.next

    def is_empty(self):
        return self.head is None

    def size(self):
        return self._size

    def print(self):
        cur = self.head
        li = []
        while cur:
            li.append(str(cur.data))
            cur = cur.next

        print(', '.join(li))
