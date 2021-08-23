# 내 풀이
def solution(scores):
    answer = ''
    people = len(scores[0])
    score_list = []

    for p in range(people):
        b = [i[p] for i in scores] # 행렬을 열에 대해서 나타냄

        if b.index(max(b)) == p: # 인덱스 b중 가장 큰 인덱스가 p이면 => 자기 자신이 평가한 점수가 가장 클 때
            a = (sum(b) - max(b)) / (len(b) - 1)
            score_list.append(a)
        elif b.index(min(b)) == p:
            a = (sum(b) - min(b)) / (len(b) - 1)
            score_list.append(a)
        else:
            a = sum(b) / len(b)
            score_list.append(a)
    print(score_list)
    for n in score_list:
        if n >= 90:
            answer = answer + 'A'
        elif 80 <= n < 90:
            answer = answer + 'B'
        elif 70 <= n < 80:
            answer = answer + 'C'
        elif 50 <= n < 70:
            answer = answer + 'D'
        elif n < 50:
            answer = answer + 'F'
    return answer

# 다른 사람 풀이
def solution1(scores):
    result = ''

    # 각 학생에게 평가된 점수를 리스트 s로 변환
    for i in range(len(scores)):
        s = []
        for j in range(len(scores)):
            s.append(scores[j][i])

        # min max에 해당하면서 유일한 값이면 해당 점수 재거
        if s[i] == min(s) and s.count(s[i]) == 1: del s[i]
        elif s[i] == max(s) and s.count(s[i]) == 1: del s[i]

        mean = sum(s) / len(s)

        if mean >= 90:
            result += 'A'
        elif mean >= 80:
            result += 'B'
        elif mean >= 70:
            result += 'C'
        elif mean >= 50:
            result += 'D'
        else:
            result += 'F'
    return result

scores = [[50,90],[50,87]]
solution(scores)
