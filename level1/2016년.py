def solution(a, b):
    answer = ''
    day = ["THU","FRI","SAT","SUN","MON","TUE","WED"]
    max = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    month = 0

    total = 0
    for idx in range(a-1):
        total = total + max[idx]
    b = total + b
    answer = day[b % 7]
    return answer

## 다른 사람 풀이
def solution(a,b):
    date = ['FRI', 'SAT', 'SUN', 'MON', 'TUE', 'WED', 'THU']
    month = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    return date[(sum(month[:a-1])+b-1) % 7]

## 다른사람 풀이 2
import datetime
def solution(a,b):
    date = ['MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT', 'SUN']
    return date[datetime.datetime(2016, a, b).weekday()] # weekday() : 정수로 요일을 반환한다. 월요일은 0~ 일요일은 6
solution(12,25)
