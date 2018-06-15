from data_structure.LinkedList import Node


# 1. n 이 주어지면 링크드리스트의 끝에서 n번째의 값을 구하라
def solution(linked_list, n):
    '''
    Hint : 두개의 포인터를 이용해보자
    - Input : n
    - Output : 끝에서 n번째 노드의 값
    '''
    list = []
    node = linked_list.head.next
    while node is not None:
        list.append(node.data)
        node = node.next

    for i in range(n):
        return list[-3]


# 2. 특정 노드를 기준으로 링크드리스트를 나누는(입력된 값을 기준으로 작은 값은 왼쪽, 큰값을 오른쪽)에 알고리즘 작성
def solution2(linked_list, target):
    '''
    - input : 6->3->8->1->5->9,   5 (리스트와 5가 주어짐)
    - ouput : 3->1->5->6->8->9  (5를 기준으로 왼쪽은 작은값이 위치하고, 오른쪽은 큰값들이 위치함)
    '''
    prev = linked_list.head
    node = linked_list.head.next
    have_met = False
    append_list = []
    prepend_list = []
    while node is not None:
        if node.data == target:
            have_met = True

        if not have_met and node.data > target:
            # append
            append_list.append(node.data)
            # delete
            prev.next = node.next
            linked_list.count -= 1
        elif have_met and node.data < target:
            # prepend
            prepend_list.append(node.data)
            # delete
            prev.next = node.next
            linked_list.count -= 1
        else:
            prev = node
        node = node.next

    node = prev
    while append_list:
        node.next = Node(append_list.pop())
        node = node.next
        linked_list.count += 1
    prev = linked_list.head
    node = linked_list.head.next
    while prepend_list:
        node = prev.next = Node(prepend_list.pop(), node)
        linked_list.count += 1


# 3. N이 주어졌을때, 1~N까지의 수에서 8이 몇번 나오는지 출력하시오
def solution3(number):
    '''
    Input : 100
    Output : 20
    Input : 1000
    Output : 300
    Input : 10000
    Output : 4000
    '''
    num = number
    digit = len(str(number))  # 자릿수
    count = 0
    # 10의 자리 이상
    for i in range(1, digit):
        count += (num / (10 ** i)) * (10 ** (i - 1))

    # 1의 자리
    if num % 10 >= 8:
        count += 1

    return int(count)


# 4. Set Of Stacks를 구현하라.
class SetOfStacks:
    '''
    접시 무더기를 생각해보자 접시무더기를 너무 높게 쌓으면 넘어질 것이다.
    그래서 높이가 특정 높이(max size)에 다다르면 새로운 무더기를 만든다. 이것이 Set Of Stacks이다
    stack이 여러개이더라도 하나인것 처럼 동작해야한다 (stack in stack)
    또한, len(), print() 등을 지원해주자.
    '''
    def __init__(self, max=10):
        self.stacks = [[], ]
        self.set_count = 0
        self.max = max
        self.top = 0

    def push(self, data):
        if int(self.top / self.max) > self.set_count:
            self.stacks.append([data])
            self.set_count += 1
        else:
            self.stacks[int(self.top / self.max)].append(data)
        self.top += 1

    def pop(self):
        self.top -= 1
        data = self.stacks[int(self.top / self.max)][int(self.top % self.max)]
        del self.stacks[int(self.top / self.max)][int(self.top % self.max)]
        return data

    def len(self):
        return self.top

    def print(self):
        print(self.stacks)


# 5. 1차원의 점들이 주어졌을 때, 그 중 가장 거리가 짧은 것의 쌍을 출력하는 함수를 작성하시오.
# (단 점들의 배열은 모두 정렬되어있다고 가정한다.)
def solution4(*args):
    prev = args[0]
    pair = None
    min = args[-1]
    for a in args[1:]:
        if min > a - prev:
            min = a - prev
            pair = [prev, a]
        prev = a
    return pair
'''
Input : (1, 3, 4, 8, 13, 17, 20)
Output (3, 4)
'''


# 6. Int값이 주어졌을때 각 자리수를 더한 값을 출력하시오
# (단, 값의 타입을 String으로 처리하는등 타입을 변경할 수 없다)
def solution5(number):
    count = 1
    sum = 0
    while number > 0:
        sum += (number % (10 ** count)) / (10 ** (count - 1))
        number -= number % (10 ** count)
        count += 1
    return number


# 7. 10미만의 자연수에서 3과 5의 배수를 구하면 3,5,6,9이다. 이들의 총합은 23이다.
# 1000미만의 자연수에서 3,5의 배수의 총합을 구하라.
def solution6(number=1000):
    multiples = []
    for i in range(1, number):
        if i % 3 == 0 or i % 5 == 0:
            multiples.append(i)
    return sum(multiples)


# 8. 10~1000까지 각 숫자 분해하여 곱하기의 전체 합 구하기
def solution7():
    '''
    예로, 10~15까지의 각 숫자 분해하여 곱하기의 전체 합은 다음과 같다.
    10 = 1 * 0 = 0
    11 = 1 * 1 = 1
    12 = 1 * 2 = 2
    13 = 1 * 3 = 3
    14 = 1 * 4 = 4
    15 = 1 * 5 = 5
    그러므로, 이 경우의 답은 0+1+2+3+4+5 = 15
    '''
    sum = 0
    for i in range(10, 1001):
        multiple = 1
        for s in str(i):
            multiple *= int(s)
        sum += multiple
    return sum


# 9. N M이라는 입력을 주면 N X M 매트릭스에 나선형 회전을 한 값을 출력해야 한다. (달팽이 문제)
def solution8(n, m):
    matrix = [[0] * n for i in range(m)]
    max_x, max_y = n-1, m-1
    min_x, min_y = 1, 0
    x, y = 0, 0
    go_vertical = False  # it means changing x
    x_move = -1
    y_move = 1
    for i in range(n * m):
        matrix[x][y] = i
        if go_vertical:
            if (x_move == 1 and x == max_x) or (x_move == -1 and x == min_x):
                if x_move == 1 and x == max_x:
                    max_x -= 1
                elif x_move == -1 and x == min_x:
                    min_x += 1
                go_vertical = False
                y_move *= -1
                y += 1 * y_move
            else:
                x += 1 * x_move
        else:
            if (y_move == 1 and y == max_y) or (y_move == -1 and y == min_y):
                if y_move == 1 and y == max_y:
                    max_y -= 1
                elif y_move == -1 and y == min_y:
                    min_y += 1
                go_vertical = True
                x_move *= -1
                x += 1 * x_move
            else:
                y += 1 * y_move

    for i in range(n):
        print(matrix[i])
'''
Input : 6 6
Ouptput :
0   1   2   3   4   5
19  20  21  22  23   6
18  31  32  33  24   7
17  30  35  34  25   8
16  29  28  27  26   9
15  14  13  12  11  10
'''

# 10. CamelCase를 snake_case 로 바꾸기!
def solution9(text):
    '''
    - Input : codingDojang
    - Output : coding_dojang
    - Input : numGoat30
    - Output: num_goat_3_0
    '''
    result = ''
    for s in text:
        if s.isupper() or s.isnumeric():
            result += '_' + s.lower()
        else:
            result += s
    return result


# 11. 모든 짝수번째 숫자만을 * 로 치환하시오.(홀수번째 숫자,또는 짝수번째 문자를 치환하면 안됩니다.)
def solution10(text):
    '''
    - Input: a1b2cde3~g45hi6
    - Output: a*b*cde*~g4*hi6
    '''
    result = ''
    for i in range(0, len(text)):
        if i % 2 != 0 and text[i].isnumeric():
            result += '*'
        else:
            result += text[i]
    return result


# 12. 양의 정수 N을 매개변수로 입력받아, *(별)문자로 높이가 N인 삼각형을 문자열로 출력하세요.
def solution11(n):
    for i in range(1, n + 1):
        print('*' * i)
'''
Input : 3
Output :
*
**
***

Input : 5
Output :
*
**
***
****
*****
'''

# if __name__ == '__main__':
#     ll = LinkedList()
#     # 6->3->8->1->5->9
#     ll.append(6)
#     ll.append(3)
#     ll.append(8)
#     ll.append(1)
#     ll.append(5)
#     ll.append(9)
#     ll.print()
#     solution2(ll, 5)
#     ll.print()