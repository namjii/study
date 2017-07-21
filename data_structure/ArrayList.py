'''
1. 데이터를 선형(Linear)으로 저장한다.
2. 데이터를 추가/삭제/검색할 수 있다.
3. 특정 인덱스의 데이터를 가지고 올 수 있다.
4. 처음 혹은 마지막 데이터를 꺼내올 수 있는 기능이 있어야 한다.
5. 리스트의 모든 데이터를 차례대로 출력할 수 있어야 한다.
'''


class ArrayList(object):
    def __init__(self):
        self.list = []
        self.count = 0

    def append(self, data):
        self.list += [data]
        self.count += 1

    def search(self, data):
        index_list = []
        for index in range(self.count):
            if data == self.list[index]:
                index_list.append(index)
        return index_list
# TODO: outofindex, valueerror raise 
    def remove(self, index):
        if 0 <= index < self.count:
            del self.list[index]
            self.count -= 1

    def get(self, index):
        if 0 <= index < self.count:
            return self.list[index]

    def pop(self):
        last = self.get(self.count - 1)
        self.remove(self.count - 1)
        return last

    def print(self):
        print(self.list)
