def solution(n,a,b):
    answer = 0
    cnt_match = 0
    num = 1
    cnt = 0
    for a in range(1, 21):
        num = num * 2
        cnt += 1
        if num == n:
            break

    for i in range(cnt):
        if a % 2 == 1:
            a = a//2 + 1
        else:
            a = a//2

        if b % 2 == 1:
            b = b//2 + 1
        else:
            b = b//2
        cnt_match += 1
        if a == b:
            break
    print(cnt_match)

    return cnt_match

# 다른 사람 풀이1
def solution1(n, a, b):
    answer = 0
    while a != b:
        a = (a+1)//2
        b = (b+1)//2
        answer += 1
    return answer

# 다른 사람 풀이2
'''
- x^y : x와 y의 exclusive or
    ex) 4^7 : 4('100')^7('111')으로 3('11')이 계산된다
- .bit_length() : 해당 비트의 자리수
    ex) '11' : 2

- 접근법 : ((a-1)^(b-1)).bit_length()
    -> 1을 빼주는 이유는 2를 나눴을 때, 같은 자리수를 맞추기 위함
'''
def solution2(n,a,b):
    return ((a-1)^(b-1)).bit_length()

n = 8
a = 4
b = 7
solution(n,a,b)
