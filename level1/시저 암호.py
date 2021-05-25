# 내 풀이
from string import ascii_lowercase, ascii_uppercase
def solution(s, n):
    answer = ''
    lower = ascii_lowercase
    upper = ascii_uppercase
    for i in range(len(s)):
        if s[i] == ' ':
            answer += ' '
        else:
            if upper.find(s[i]) != -1:
                u = upper.find(s[i])
                answer += upper[(u + n) % 26]
                continue

            else:
                l = lower.find(s[i])
                answer += lower[(l + n) % 26]
    print(answer)
    return answer

# 다른 사람 풀이
def solution1(s, n):
    s = list(s)
    for i in range(len(s)):
        if s[i].isupper():
            s[i] = chr((ord(s[i]) - ord('A') + n) % 26 + ord('A'))
        elif s[i].islower():
            s[i] = chr((ord(s[i]) - ord('a') + n) % 26 + ord('a'))
    return ''.join(s)
'''
chr() 함수는 숫자를 인자로 주면 아스키 코드에 해당하는 문자를 반환 (아스키 코드 -> 문자)
ord() 함수는 문자의 아스키 코드를 반환한다(문자 -> 아스키 코드)
'''

s = "a B z"
n = 4
solution(s, n)
