def solution(price, money, count):
    answer = -1
    summ = 0
    for i in range(1, count + 1):
        summ = price * i
    if money >= summ:
        answer = 0
    else:
        answer = summ - money

    return answer

# 다른 사람 풀이1
def solution1(price, money, count):
    return abs(min(money-sum([i*price for i in range(1, count+1)]),0))


price = 3
money = 20
count = 4
solution(price, money, count)
