import numpy

def solution(answers):
    answer = [] # 가장 많은 문제를 맞힌 사람

    one = []
    two = []
    three = []

    one_count = 0
    two_count = 0
    three_count = 0

    answers = numpy.array(answers)
    a_len = answers.shape[0] # 문제 수

    # 수포자 1의 찍는 방식
    for i in range(a_len):
        if divmod(i+1 , 5)[1] == 1:
            one.append(1)
        elif divmod(i+1 , 5)[1] == 2:
            one.append(2)
        elif divmod(i+1 , 5)[1] == 3:
            one.append(3)
        elif divmod(i+1 , 5)[1] == 4:
            one.append(4)
        elif divmod(i+1 , 5)[1] == 0:
            one.append(5)

    # 수포자 2의 찍는 방식
    for i in range(a_len):
        if divmod(i+1 , 2)[1] == 1:
            two.append(2)
        elif divmod(i+1 , 2)[1] == 0:
            if len(two) < 2:
                two.append(1)
            else:
                if two[-2] == 1:
                    two.append(3)
                elif two[-2] == 3:
                    two.append(4)
                elif two[-2] == 4:
                    two.append(5)
                elif two[-2] == 5:
                    two.append(1)
    # print(two)
    # 수포자 3의 찍는 방식
    for i in range(a_len):
        if len(three) < 2:
            three.append(3)
        else:
            if divmod(i+1 , 2)[1] == 0:
                three.append(three[-1])
            elif divmod(i+1 , 2)[1] == 1:
                if three[-1] == 3:
                    three.append(1)
                elif three[-1] == 1:
                    three.append(2)
                elif three[-1] == 2:
                    three.append(4)
                elif three[-1] == 4:
                    three.append(5)
                elif three[-1] == 5:
                    three.append(3)
    # 정답 개수 세기
    for i in range(a_len):
        if answers[i] == one[i]:
            one_count = one_count + 1
        if answers[i] == two[i]:
            two_count = two_count + 1
        if answers[i] == three[i]:
            three_count = three_count + 1

    # 가장 높은 점수를 얻은 학생 구하기
    winner = max(one_count, two_count, three_count)
    if winner == one_count:
        answer.append(1)
    if winner == two_count:
        answer.append(2)
    if winner == three_count:
        answer.append(3)

    return answer


answers = [1,2,3,4,5]
solution(answers)

