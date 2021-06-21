'''
1. 처움엔 set() 함수를 통해 집합으로 생성하려 했지만 그럴경우 중복되는 원소를 모두 삭제하기 때문에 자카드 유사도를 구할 수 없다.
2. Counter() 사용함
3 .문제 조건에서 대문자와 소문자의 차이를 무시한다는 조건이 있었으므로 str1과 str2 모두 소문자로 변환  str1.lower()
4. str1, str2의 문자열에서 두글자씩 끊은 결과를 저장한 a,b가 모두 영어 알파벳일 경우만 a,b의 값을 각각 리스트 st1과 st2에 저장
5. 리스트 형태의 st1과 st2를 각각 Counter 객체로 변환시켜준다.
-> Counter()은 각각의 리스트의 원소값을 Key값으로 하고, 원소의 개수를 value 값으로 하는 dictionary 형태의 구조를 반환
-> ex) Counter({'fr': 1, 'ra': 1, 'an': 1, 'nc': 1, 'ce': 1})
6. 각각의 Counter 객체에서 교집합과 합집합을 나타내는 변수인 g와 h에 교집합 합집합 결과 저장
-> ex) g : Counter({'fr': 1, 'nc': 1}), h : Counter({'fr': 1, 'ra': 1, 'an': 1, 'nc': 1, 'ce': 1, 're': 1, 'en': 1, 'ch': 1})
7. 필요한것은 각각의 key값에 해당하는 원소값이므로 elements()를 사용해 원소값만을 추출해 list로 변환
'''


from collections import Counter
def solution(str1, str2):
    answer = 0
    st1 = []
    st2 = []
    str1 = str1.lower()
    str2 = str2.lower()
    for s1 in range(len(str1)):
        if s1 < len(str1) -1:
            a = str1[s1:s1+2]
            # if a.isalnum(): # 문자열 안에 특수문자가 들어가 있으면 False 반환
            if a.isalpha():
                st1.append(a)
        count1 = Counter(st1)


    for s2 in range(len(str2)):
        if s2 < len(str2) -1:
            b = str2[s2:s2+2]
            if b.isalpha():
                st2.append(b)
        count2 = Counter(st2)

    g = count1 & count2
    h = count1 | count2

    if len(list(g.elements())) * len(list(h.elements())) == 0:
        answer = 65536
    else:
        answer = int(len(list(g.elements())) / len(list(h.elements())) * 65536)

    print(answer)
    return answer

# 다른사람 풀이1
import re
import math
def solution1(str1, str2):
    # 두칸씩 쪼갠 값이 모두 문자이면 str1, str2에 append
    str1 = [str1[i:i+2].lower() for i in range(0, len(str1) - 1) if not re.findall('[a-zA-Z]+',str1[i:i+2])]
    str2 = [str2[i:i+2].lower() for i in range(0, len(str2) - 1) if not re.findall('[a-zA-Z]+',str2[i:i+2])]

    # 합집합과 교집합
    gyo = set(str1) & set(str2)
    hap = set(str1) & set(str2)

    # 합집합이 0이면 65536 출력
    if len(hap) == 0:
        return 65536

    # 교집합과 합집합의 counter를 따로 계산
    gyo_sum = sum([min(str1.count(gg), str2.count(gg)) for gg in gyo])
    hap_sum = sum([max(str1.count(hh), str2.count(hh)) for hh in hap])

    return math.floor((gyo_sum / hap_sum) * 65536)
str1 = 'FRANCE'
str2 = 'french'
solution1(str1, str2)
