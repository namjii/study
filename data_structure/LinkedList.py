class Node(object):
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

'''
1. 데이터를 선형(Linear)으로 저장한다.
2. 데이터를 추가/삭제/검색할 수 있다.
3. 특정 인덱스의 데이터를 가지고 올 수 있다.
4. 처음 혹은 마지막 데이터를 꺼내올 수 있는 기능이 있어야 한다.
5. 리스트의 모든 데이터를 차례대로 출력할 수 있어야 한다.
'''


class LinkedList(object):
    def __init__(self):
        self.head = Node('head')
        # head는 count에서 세지않음
        self.count = 0

    def append(self, data):
        node = self.head
        for i in range(self.count):
            node = node.next
        node.next = Node(data=data)
        self.count += 1

    def search(self, data):
        index_list = []
        node = self.head
        for i in range(self.count):
            node = node.next
            if node.data == data:
                index_list.append(i)
        return index_list

    def remove(self, index):
        if 0 <= index < self.count:
            prev = self.head
            node = self.head.next
            for i in range(index):
                prev = node
                node = node.next
            prev.next = node.next
            self.count -= 1

    def get(self, index):
        if 0 <= index < self.count:
            node = self.head.next
            for i in range(index):
                node = node.next
            return node.data

    def pop(self):
        last = self.get(self.count - 1)
        self.remove(self.count - 1)
        return last

    def print(self):
        node = self.head
        for i in range(self.count):
            node = node.next
            print(node.data)

