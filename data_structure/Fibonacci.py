

# 피보나치 수의 n번째 숫자 구하기
# 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584 ...
def fibonacci(n):
    '''
    피보나치 수는 0과 1로 시작하며, 다음 피보나치 수는 바로 앞의 두 피보나치 수의 합이 된다.
    '''
    if n <= 0:
        raise ValueError("0 보다 큰 수를 입력하세요")
    else:
        if n == 1:
            return 0
        elif n == 2:
            return 1
        else:
            return fibonacci(n-1) + fibonacci(n-2)

