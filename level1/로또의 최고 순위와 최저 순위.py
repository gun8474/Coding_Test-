def solution(lottos, win_nums):
    answer = []
    cnt = 0
    for i in range(len(lottos)):
        for j in range(len(win_nums)):
            if lottos[i] == win_nums[j]:
                cnt += 1
                win_nums[j] = 100 # 이미 맞춘 로또 번호임을 나타내기 위함

    max = cnt
    min = cnt
    for a in range(len(lottos)):
        for b in range(len(win_nums)):
            if lottos[a] == 0:
                if win_nums[b] != 100:
                    lottos[a] = win_nums[b]
                    max += 1

    else:
        max = 7-max
        min = 7-min
    if max == 7:
        max = 6
    if min == 7:
        min = 6
    answer = [max, min]
    print(answer)
    return answer

# 다른 사람 풀이
def solution(lottos, win_nums):
    rank = {6:1, 5:2, 4:3, 3:4, 2:5, 1:6, 0:6}
    cnt = 0
    super = lottos.count(0) # lottos 리스트에서 0의 개수 세기
    for i in lottos:
        if i in win_nums:
            cnt+=1
    return[rank[cnt+super], rank[cnt]]

# 다른 사람 풀이2
from collections import Counter

def solution (lottos, win_nums):
    lotto = {6:1, 5:2, 4:3, 3:4, 2:5, 1:6, 0:6}
    c = Counter(lottos) - Counter(win_nums) # win_nums에 포함되지 않는 lottos의 원소들의 종류와 개수
    cnt = 6 - sum([v for k, v in c.items()])  # c.items()는 win_nums에 포함되지 않는 lottos의 원소들의 종류(k)와 개수(v)의 짝을 반환
                                              # cnt 는 맞춘 숫자의 개수
    return [lotto[cnt + c[0]], lotto[cnt]]
'''Counter 함수 예시
list = ['Hello', 'HI', 'How', 'When', 'Where', 'Hello']
Counter(list) --> Counter({'Hello': 2, 'HI': 1, 'How': 1, 'When': 1, 'Where': 1})

value = "Hello Appia"
Counter(value) --> Counter({'l': 2, 'p': 2, 'H': 1, 'e': 1, 'o': 1, ' ': 1, 'A': 1, 'i': 1, 'a': 1})
'''


lottos = [44, 1, 0, 0, 31, 25]
win_nums = [31, 10, 45, 1, 6, 19]
solution(lottos, win_nums)
