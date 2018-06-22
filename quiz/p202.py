

# 21. 다음과 같은 형태의 배열을 다음과 같은 형태로 바꾸시오.
# [a1,a2,a3...,an,b1,b2...bn] => [a1,b1,a2,b2.....an,bn] , 단, 공간복잡도는 O(1)
def solution21(origin):
    # origin = ['a1', 'a2', 'a3', 'b1', 'b2', 'b3']
    length = len(origin)
    divide = 0  # 3
    for i in range(1, length):
        if origin[i-1][0] != origin[i][0]:
            divide = i - length
            break

    for i in range(0, int(length/2) - 1):  # 1 2 3(X)
        # -3 - 2 -1
        pop = origin.pop(divide + i)
        origin[i * 2 + 2:] = origin[i * 2 + 1:]
        origin[i * 2 + 1] = pop
    return origin
# ['a1', 'a2', 'a3', 'b1', 'b2', 'b3'] input index:1  delete index:3(-3)
# ['a1', 'b1', a2', 'a3', 'b2', 'b3'] input index:3  delete index:4(-2)
# ['a1', 'b1', a2', 'b2', 'a3', 'b3']
solution21(['a1', 'a2', 'a3', 'b1', 'b2', 'b3'])
solution21(['a1', 'a2', 'a3', 'a4', 'b1', 'b2', 'b3', 'b4'])


# 22. getMiddle메소드는 하나의 단어를 입력 받습니다.
# 단어를 입력 받아서 가운데 글자를 반환하도록 getMiddle메소드를 만들어 보세요.
# 단어의 길이가 짝수일경우 가운데 두글자를 반환하면 됩니다.
# 예를들어 입력받은 단어가 power이라면 w를 반환하면 되고, 입력받은 단어가 test라면 es를 반환하면 됩니다.
def solution22(word):
    length = len(word)
    half = int(length/2)

    if length % 2 == 0:
        return word[half - 1:half + 1]
    else:
        return word[half]
solution22('power')
solution22('test')
solution22('applemango')


# 23. n개의 정수를 가진 배열이 있다. 이 배열은 양의 정수와 음의 정수를 모두 가지고 있다.
# 이제 당신은 이 배열을 좀 특별한 방법으로 정렬해야 한다.
# 정렬이 되고 난 후, 음의 정수는 앞쪽에 양의정수는 뒷쪽에 있어야 한다.
# 또한 양의정수와 음의정수의 순서에는 변함이 없어야 한다.
def solution23(list):
    '''
    - Input : -1 1 3 -2 2
    - Output : -1 -2 1 3 2

    input : 1 -2 3 -1 2
    output : -2 -1 1 3 2
    '''
    index = 0
    for i in range(len(list)):
        if list[index] > 0:
            pop = list.pop(index)
            list.append(pop)
        else:
            index += 1
    return list
solution23([-1, 1, 3, -2, 2])
solution23([1, -2, 3, -1, 2])


# 24. String이 주어지면, 중복된 char가 없는 가장 긴 서브스트링 (substring)의 길이를 찾으시오.
def solution24(word):
    unique = word[0]
    largest = word[0]
    for s in word[1:]:
        if s in unique:
            unique = s
        else:
            unique += s
            if len(largest) < len(unique):
                largest = unique
    return largest
'''
- Input: "aabcbcbc"
- Output: 3 // "abc"

- Input: "aaaaaaaa"
- Output: 1 // "a"

- Input: "abbbcedd"
- Output: 4 // "bced"
'''
solution24('aabcbcbc')
solution24('aaaaaaaa')
solution24('abbbcedd')


# 25. strange_sort함수는 strings와 n이라는 매개변수를 받아들입니다.
# strings는 문자열로 구성된 리스트인데, 각 문자열을 인덱스 n인 글자를 기준으로 정렬하면 됩니다.
# 예를들어 strings가 ["sun", "bed", "car"]이고 n이 1이면 각 단어의 인덱스 1인 문자 u, e ,a를 기준으로 정렬해야 하므로 결과는 ["car", "bed", "sun"]이 됩니다.
# strange_sort함수를 완성해 보세요.
def solution25(strings, num):
    for i in range(len(strings)):  # selection sort
        min = i
        for j in range(i + 1, len(strings)):
            if ord(strings[j][num]) < ord(strings[min][num]):
                min = j
        strings[i], strings[min] = strings[min], strings[i]
    return strings
solution25(['sun', 'bed', 'car'])


# 26. 2이상 1000이하 자연수의 집합에서 소수의 개수를 구하는 알고리즘을 작성하시오.
def solution26():
    sum = 0
    for i in range(2, 1001):
        is_prime = True
        for j in range(2, i):
            if i % j == 0:
                is_prime = False
                break
        if is_prime:
            sum += 1
    return sum


# 27. no_continuous함수는 스트링 s를 매개변수로 입력받습니다. s의 글자들의 순서를 유지하면서,
# 글자들 중 연속적으로 나타나는 아이템은 제거된 배열(파이썬은 list)을 리턴하도록 함수를 완성하세요.
# 예를들어 다음과 같이 동작하면 됩니다.
def solution27(word):
    prev = word[0]
    result = word[0]
    for s in word[1:]:
        if prev != s:
            result += s
        prev = s
    return result
'''
s가 '133303'이라면 1303를 리턴
s가 '47330'이라면 4730을 리턴
'''
solution27('133303')
solution27('47330')


# 28. 어떤 수를 입력받아 그 수의 약수를 모두 더한 수 sumDivisor 함수를 완성해 보세요.
# 예를 들어 12가 입력된다면 12의 약수는 [1, 2, 3, 4, 6, 12]가 되고, 총 합은 28이 되므로 28을 반환해 주면 됩니다.
def solution28(num):
    sum = 0
    for i in range(1, num + 1):
        if num % i == 0:
            sum += i
    return sum
solution28(12)
solution28(18)


# 29. water_melon함수는 정수 n을 매개변수로 입력받습니다.
# 길이가 n이고, 수박수박수...와 같은 패턴을 유지하는 문자열을 리턴하도록 함수를 완성하세요.
# 예를 들어 n이 4이면 '수박수박'을 리턴하고 3이라면 '수박수'를 리턴하면 됩니다.
def solution29(num):
    result = '수박' * int(num / 2)
    if num % 2 != 0:
        result += '수'
    return result
solution29(4)
solution29(3)


# 30. strToInt 메소드는 String형 str을 매개변수로 받습니다. str을 숫자로 변환한 결과를 반환하도록 strToInt를 완성하세요.
# 예를 들어 str이 "1234"이면 1234를 반환하고, "-1234"이면 -1234를 반환하면 됩니다.
# str은 부호(+,-)와 숫자로만 구성되어 있고, 잘못된 값이 입력되는 경우는 없습니다.
# (언어에 미리 정의된 strToInt를 사용하지 못함)
def solution30(str):
    result = 0
    for s in str:
        if result != 0:
            result *= 10
        if not s.isnumeric():
            continue
        result += ord(s) - 48
    if str[0] == '-':
        result *= -1
    return result
solution30('-1234')
solution30('1234')


# 31. 정수 배열(int array)과 정수 N이 주어지면, N번째로 큰 배열 원소를 찾으시오.
def solution31(list, num):
    for i in range(num):  # bubble sort
        for j in range(len(list)-1-i):
            if list[j] > list[j+1]:
                list[j], list[j+1] = list[j+1], list[j]
    return list[-num]
'''
- Input: [-1, 3, -1, 5, 4], 2
- Output: 4

- Input: [2, 4, -2, -3, 8], 1
- Output: 8

- Input: [-5, -3, 1], 3
- Output: -5
'''
solution31([-1, 3, -1, 5, 4], 2)
solution31([2, 4, -2, -3, 8], 1)


# 32 아래 조건에 따라 리스트를 회전하는 프로그램을 작성하시오.

# 조건
# 입력값은 한 행의 문자열로 주어지며, 각 값은 공백으로 구분된다.
# 첫 번째 값은 리스트를 회전하는 양과 방향(음수의 경우 좌측으로, 양수의 경우 우측으로 회전)이다.
# 첫 번째 값을 제외한 나머지 값은 리스트의 각 항목의 값이다.
# 회전된 리스트를 문자열로 출력한다.
# 구현에 이용할 자료구조에 대한 조건이나 제약은 없다.
# 입력되는 리스트의 항목의 개수는 유한한다.
def solution32(word):
    list = word.split(' ')
    key = int(list.pop(0))
    # if key > 0:
    #     list = list[-key:] + list[:key-1]
    # elif key < 0:
    #     list = list[-key:] + list[:-key]
    if key > 0:
        for i in range(key):
            list.insert(0, list.pop())
    elif key < 0:
        for i in range(-key):
            list.append(list.pop(0))
    return ' '.join(list)
# 예 1)
# 입력: 1 10 20 30 40 50
# 출력: 50 10 20 30 40
solution32('1 10 20 30 40 50')
# 예 2)
# 입력: 4 가 나 다 라 마 바 사
# 출력: 라 마 바 사 가 나 다
solution32('4 가 나 다 라 마 바 사')
# 예 3)
# 입력: -2 A B C D E F G
# 출력: C D E F G A B
solution32('-2 A B C D E F G')
# 예 4)
# 입력: 0 똘기 떵이 호치 새초미
# 출력: 똘기 떵이 호치 새초미
solution32('0 똘기 떵이 호치 새초미')


# 33
# 길이가 같은 두 문자열(string) A 와 B가 주어지면, A 가 B 로 1:1 암호화 가능한지 찾으시오.
def solution33(a, b):
    dic = {}
    for i in range(len(a)):
        if a[i] not in dic:
            dic[a[i]] = b[i]
        else:
            if dic[a[i]] != b[i]:
                return False
    return True
# Input: "EGG", "FOO"
# Output: True // E->F, G->O
solution33("EGG", "FOO")
# Input: "ABBCD", "APPLE"
# Output: True // A->A, B->P, C->L, D->E
solution33("ABBCD", "APPLE")
# Input: "AAB", "FOO"
# Output: False
solution33("AAB", "FOO")


# 34
# 정수로된 배열이 주어지면, 각 원소가 자신을 뺀 나머지 원소들의 곱셈이 되게하라.
# 단, 나누기 사용 금지, O(n) 시간복잡도

# input: [1, 2, 3, 4, 5]
# output: [120, 60, 40, 30, 24]
def solution34(list):
    mul = 1
    for value in list:
        mul *= value

    for i in range(len(list)):
        list[i] = int(mul / list[i])
    return list

# 35
# digit_reverse함수는 양의 정수 n을 매개변수로 입력받습니다.
# n을 뒤집어 숫자 하나하나를 list로 표현해주세요
# 예를 들어 n이 12345이면 [5,4,3,2,1]을 리턴하면 됩니다.
def solution35(n):
    return [i for i in range(n, 0, -1)]

solution35(5)
