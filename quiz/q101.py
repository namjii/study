

# 1. 문자열에 포함된 문자들이 전부 유일한 지 검사하는 알고리즘
import collections


def has_unique_character(text):
    '''
    1. Input : abcdefg / Output : True
    2. Input : text / Output : false
    '''
    # return len(text) == len(set(list(text)))
    dic = {}
    for t in text:
        if t in dic:
            return False
        dic[t] = 0
    return True


# 2. 문자열 뒤집기 알고리즘
def reverse_text(text):
    '''
    1. Input : txt / Output : txt
    2. Input : text / Output : txet
    '''
    for i in range(len(text)/2):
        text[i], text[len(text)-i-1] = text[len(text)-i-1], text[i]
    return text


# 3. anagram, 문자열 2개 입력 받아 순열(조합)인지 판별하는 메서드. 즉 두 word가 동일한 캐릭터의 조합으로 만들어졌는가?
def is_anagram(text1, text2):
    '''
    1. Input : show, owsh  / Output : true
    2. Input : item, meet / Output : false
    '''
    # dic = {}
    # for t in text1:
    #     if t not in dic:
    #         dic[t] = 0
    #     else:
    #         dic[t] += 1
    #
    # for t in text2:
    #     if t not in dic or dic[t] <= 0:
    #         return False
    #     else:
    #         dic[t] -= 1
    if len(text1) == len(text2):
        text1 = sorted(text1)
        text2 = sorted(text2)

        for i, j in zip(text1, text2):
            if i != j:
                return False
    else:
        return False
    return True


# 4. 같은 문자 반복 횟수를 이용한 문자열 압축
def solution(text):
    '''
    input : aabcccaa
    output : a2b1c3a2
    '''
    prev = ''
    count = 1
    result = ''

    for t in text:
        if prev != t:
            if prev != '':
                result += prev + str(count)
            prev = t
            count = 1
        else:
            count += 1
    result += prev + str(count)
    return result


# 5. 링크드리스트에서 중복 문자(데이터) 제거하기
def solution2(linked_list):
    '''
    0~9까지의 문자로 된 숫자를 입력 받았을 때, 이 입력 값이 0~9까지의 숫자가 각각 한 번 씩만 사용된 것인지 확인하는 함수를 구하시오.

    sample inputs: 0123456789 01234 01234567890 6789012345 012322456789
    sample outputs: true false false true false
    '''
    dic = {}
    node = prev = linked_list.head
    while node is not None:
        if node.data not in dic:
            dic[node.data] = True
        else:
            prev.next = node.next
        prev = node
        node = node.next
    return linked_list


# 6. 괄호의 사용이 잘 되었는지 잘못 되었는지 판별 해 주는 프로그램을 작성하시오.
'''
다음은 정상적인(balanced) 괄호 사용의 예이다.
(()()()())
(((())))
(()((())()))

다음은 비정상적인(not balanced) 괄호 사용의 예이다.
((((((())
()))
(()()(()
(()))(
())(()
'''

# 7.
'''
A씨는 두 개의 버전을 비교하는 프로그램을 작성해야 한다.
버전은 다음처럼 "." 으로 구분된 문자열이다.
버전 예) 1.0.0, 1.0.23, 1.1

두 개의 버전을 비교하는 프로그램을 작성하시오.
다음은 버전 비교의 예이다.

0.0.2 > 0.0.1
1.0.10 > 1.0.3
1.2.0 > 1.1.99
1.1 > 1.0.1
'''

# 8.
'''
내이름은 리효리 거꾸로 해도 리효리
단, linkedlist에 저장되어 있다

input : 1 -> 3 -> 1
output : True

input : 1 -> 5 -> 3
output : False
'''