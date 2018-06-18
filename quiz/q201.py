# 13. 양의 정수 N을 매개변수로 입력받아, *(별)문자로 높이가 N인 정삼각형을 문자열로 출력하세요.
def solution13(n):
    for i in range(n):
        print(' ' * (n - i - 1) + "*" * (1 + 2 * i))


# 14. input은 int n을 입력 받아 첫번째 row는 (n-1)의 O와 X,
# 두번째 row는 (n-2)의 O와 XX, 세번째 row는 (n-3)의 0와 XXX... n번째 row는 n의 X을 출력하시오.
def solution14(n):
    for i in range(n):
        y = i + 1
        x = n - y
        print('X' * x + 'O' * y)


# 15. 두개의 정렬된(sorted) 정수 링크드리스트(linked list)가 주어지면, 두 리스트를 합친 정렬된 링크드리스트를 만드시오.
'''
Input: 1->2->3, 1->2->3
Output: 1->1->2->2->3->3

Input: 1->3->5->6, 2->4
Output: 1->2->3->4->5->6
'''
def solution15(l1, l2):
    p1_prev = None
    p1 = l1.head
    p2 = l2.head

    while p1 is not None:
        if p1 >= p2:
            p1_prev = p1
            p1 = p1.next
        else:
            p2_temp = p2
            p1_prev.next = p2
            p2.next = p1
            p1.prev = p2
            p2 = p2_temp
    p1_prev.next = p2


# 16. 정수(int)가 주어지면, 팰린드롬(palindrome)인지 알아내시오.
# 팰린드롬이란, 앞에서부터 읽으나 뒤에서부터 읽으나 같은 단어를 말합니다. 단, 정수를 문자열로 바꾸면 안됩니다.
def solution16(number):
    origin = number
    reverse = 0

    while number > 0:
        reverse *= 10
        reverse += number % 10
        number = int(number / 10)
    return origin == reverse
'''
Input: 12345
Output: False

Input: -101
Output: False

Input: 11111
Output: True

Input: 12421
Output: True
'''


# 17. 정수 배열(int array)이 주어지면 0이 아닌 정수 순서를 유지하며 모든 0을 배열 오른쪽 끝으로 옮기시오.
# 단, 시간복잡도는 O(n), 공간복잡도는 O(1)여야 합니다.
def solution17(list):
    z = None
    for i in range(len(list)):
        if list[i] == 0:
            z = i
            break
    for i in range(z+1,len(list)):
        if list[i] != 0:
            list[i], list[z] = list[z], list[i]
            z += 1
    return list
'''
Input: [0, 5, 0, 3, -1]
Output: [5, 3, -1, 0, 0]

Input: [3, 0, 3]
Output: [3, 3, 0]
'''


# 18. 정수 배열(int array)이 주어지면 두번째로 큰 값을 프린트하시오.
def solution18(list):
    first = list[0]
    second = None
    for li in list[1:]:
        if first < li:
            second = first
            first = li
        elif first > li:
            if second is None or second < li:
                second = li
    if second is None:
        return 'Does Not Exist'
    else:
        return second
'''
- Input: [10, 5, 4, 3, -1]
- Output: 5
- Input: [3, 3, 3]
- Output: Does not exist.
'''


# 19. 정수 배열과 타겟 숫자가 주어지면, 합이 타겟값이 되는 두 원소의 인덱스를 찾으시오. 단, 시간복잡도 O(n) 여야 합니다.
def solution19(list, target):
    dic = {}
    for i in range(len(list)):
        dic[list[i]] = i
        if target - list[i] in dic:
            return [i, dic[target - list[i]]]
'''
- Input: [2, 5, 6, 1, 10], 타겟 8
- Output: [0, 2] // 배열[0] + 배열[2] = 8
'''


# 20. 피보나치 배열은 0과 1로 시작하며, 다음 피보나치 수는 바로 앞의 두 피보나치 수의 합이 된다.
# 정수 N이 주어지면, N보다 작은 모든 짝수 피보나치 수의 합을 구하여라.
def solution20(n):
    a = 0
    b = 1
    sum = 0
    while a + b < n:
        if (a + b) % 2 == 0:
            sum += (a + b)
        a, b = b, a + b
    return sum
'''
- Input: N = 12
- Output: 10 // 0, 1, 2, 3, 5, 8 중 짝수인 2 + 8 = 10.
'''

