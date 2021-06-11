import math
def solution(n):
    answer = 0
    if int(n**0.5) == n**0.5:
        n = math.sqrt(n)
        answer = (n+1) ** 2
    else:
        return -1
    return answer

# 다른 사람 풀이1
def solution1(n):
    sqrt = n ** (1/2)

    if sqrt % 1 == 0: # 값이 소수가 아닐 때
        return (sqrt + 1) ** 2
    return 'no'

"""
1. 제곱근을 구할 때 import math를 통해 모듈을 import 하고 math.sqrt() 함수를 통해 제곱근을 구할 수 있다.
 """

n = 121
solution(n)
