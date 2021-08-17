import operator

# 내풀이
def solution(s):
    answer = ''
    s_list = []
    sidx_list = []

    i_list = []
    iidx_list = []
    string_num = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    int_num = ['0','1','2','3','4','5','6','7','8','9']

    for string in range(len(string_num)):
        val_string = s.find(string_num[string])
        if val_string != -1:
            s_list.append(val_string)
            sidx_list.append(string)
    s_list = dict(zip(s_list, sidx_list))


    for i in range(len(int_num)):
        val_int = s.find(int_num[i])
        if val_int != -1:
            i_list.append(val_int)
            iidx_list.append(i)
    i_list = dict(zip(i_list, iidx_list))

    s_list.update(i_list) # 두 개의 딕셔너리 합치기
    s_list = sorted(s_list.items(), key=operator.itemgetter(0))
    for r in range(len(s_list)):
        answer += str(s_list[r][1])
    return answer

# 다른 사람 풀이1
def solution1(s):
    answer = s
    num_s = {'zero':0, 'one':1, 'two':2, 'three':3, 'four':4, 'five':5, 'six':6, 'seven':7, 'eight':8, 'nine':9}

    for item in num_s.item():
        answer = answer.replace(item[0], str(item[1]))
    return int(answer)

# 다른 사람 풀이2
def solution2(s):
    answer = ''
    dict = {
        'zero': 0, 'one': 1, 'two': 2, 'three': 3,
        'four': 4, 'five': 5, 'six': 6, 'seven': 7,
        'eight': 8, 'nine': 9
    }

    answer = s
    for key, value in dict.items():
        answer = answer.replace(key, value)
    return int(answer)

s = 'one4seveneight'
solution(s)

