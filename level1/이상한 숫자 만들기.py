def solution(s):
    answer = ''
    s = s.split(' ')
    for word in s:
        for alpha in range(len(word)):
            if alpha % 2 == 0:
                result = word[alpha].upper() # 문자열.upper()를 하면 원본 문자열은 대문자로 바뀌지 않는다/ 그러므로 result 변수에 대문자로 변환된 것을 저장
            else:
                result = word[alpha]
            answer = answer + result # 홀수번째 인덱스와 짝수번째 인덱스를 번갈아면서 answer에 저장함
        answer = answer + ' ' # 띄어쓰기로 구분된 단어들을 기준으로 띄어줌
    return answer

"""
문자열과 튜플은 그 요소 값을 변경할 수 없는 immutable한 자료형이다.
-> 문자열은 리스트와 달리 string[3] = 'k' 와 같이 요소를 변경할 수 없다.
-> 대신 slicing이나 replace() 등등을 통해 값을 변경할 수 있다.
"""
# 다른 사람 풀이1
def solution1(s):
    s_split = s.split(' ')
    for k in range(len(s_split)):
        s_list = list(s_split[k])

        for i in range(len(s_list)):
            if i % 2 == 0:
                s_list[i] = s_list[i].upper()
            elif i % 2 == 1:
                s_list[i] = s_list[i].lower()
        s_split[k] = "".join(s_list)

    answer = "".join(s_split)
    return answer

# 다른 사람 풀이2
def solution2(s):
    return ' '.join([''.join([c.upper() if i % 2 == 0 else c.lower() for i, c in enumerate(w)]) for w in s.split(' ')])
s = 'try hello world'
solution(s)
