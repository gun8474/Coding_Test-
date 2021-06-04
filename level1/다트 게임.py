# 내 풀이
import re
def solution(dartResult):
    answer = []
    p = re.compile("(\d+)([a-zA-Z])(\*|#)?") # 1번째 : 두자리 포함 숫자 추출, 2번째 : 모든 대소문자 영어 추출, 3번째 : *, | 또는 or, # 추출
                                            # ? : 3번째 뒤어 붙은 물음표는 3번째는 있어도 되고 없어도 된다는 뜻
    result = p.findall(dartResult) # "\d" -> 문자열에서 숫자를 한자리씩 추출, "\d+" -> 문자열에서 숫자를 두자리 포함해서 추출

    for idx, score in enumerate(result):
        point = score[0]
        option = score[1]
        effect = score[2]

        if option == 'S':
            answer.append(int(point))
        elif option == 'D':
            answer.append(int(point) ** 2)
        elif option == 'T':
            answer.append(int(point) ** 3)
        print(answer)
        if effect == '*':
            if len(answer) == 1:
                answer[0] = answer[0] * 2
            else:
                answer[-2] = answer[-2] * 2
                answer[-1] = answer[-1] * 2

        if effect == '#':
            if len(answer) == 1:
                answer[0] = answer[0] * -1
            else:
                # answer[-2] = answer[-2] * 2
                answer[-1] = answer[-1] * -1
        if effect == '':
            continue
    result = sum(answer)
    return result

## 다른사람 풀이1
import re
def solution1(dartResult):
    bonus = {'S': 1, 'D': 2, 'T': 3}
    option = {'': 1, '*': 2, '#': -1}
    p = re.compile('(\d+)([SDT])([*#]?)')
    dart = p.findall(dartResult)
    for i in range(len(dart)):
        if dart[i][2] == '*' and i>0: # 각각의 3번의 기회 중 option
            dart[i-1] *= 2
        dart[i] = int(dart[i][0]) ** bonus[dart[i][1]] * option[dart[i][2]]

    answer = sum(dart)
    return answer


dartResult = '1D2S3T*'
solution1(dartResult)
