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
        for i in range(self.count + 1):
            if node.data == data:
                index_list.append(i)
            node = node.next
        return index_list

    def remove(self, index):
        if 0 == index:
            print('head 는 삭제할 수 없습니다.')
        if 0 < index <= self.count:
            # index : head(0) -> 1 -> 2...
            node = self.head
            prev = None
            for i in range(index):
                prev = node
                node = node.next

            prev.next = node.next
            self.count -= 1

    def get(self, index):
        if 0 <= index <= self.count:
            node = self.head
            for i in range(index):
                node = node.next
            return node.data

    def pop(self):
        node = self.head
        prev = None
        if 0 < self.count:
            for i in range(self.count):
                prev = node
                node = node.next

            prev.next = node.next
            self.count -= 1
            return node.data

    def print(self):
        node = self.head
        for i in range(self.count):
            node = node.next
            print(node.data)
