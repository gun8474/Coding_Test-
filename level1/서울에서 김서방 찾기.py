def solution(seoul):
    for i in range(len(seoul)):
        if seoul[i] == 'Kim':
            count = i
            break
    answer = '김서방은 ' + str(count) + '에 있다'
    print(answer)
    return answer

# 다른사람 풀이
def solution1(seoul):
    return '김서방은 {}에 있다'.format(seoul.index("Kim"))

seoul = ["Jane", "Kim"]
solution(seoul)
