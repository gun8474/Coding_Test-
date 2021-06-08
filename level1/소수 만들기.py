# 소수임을 판별하는 함수
def prime_number(number):
    if number != 1:
        for i in range(2,number):
            if number % i == 0:
                return False
    else:
        return False

    return True

# 내 풀이 -> 소수 판별 함수를 사용함
def solution(nums):
    answer = -1
    result = 0
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            for k in range(j+1, len(nums)):
                sum = nums[i] + nums[j] + nums[k]
                if prime_number(sum) == True:
                    result+=1
    return result


# 다른 사람 풀이1
'''
*포인트*
combination() --> 중복을 허용하지 않고 순서 의미가 있는 조합을 리턴해줌
'''
from itertools import combinations

def solution1(nums):
    answer = 0
    cmb = list(combinations(nums,3)) # nums 배열을 3개씩 조합 후 list로 변경
    for arr in cmb:
        if prime_number(sum(arr)): # cmb를 하나씩 가져와서 sum한 값을 소수 판별 함수애 대입
            answer+=1
    return answer
nums = [1,2,7,6,4]
solution(nums)
