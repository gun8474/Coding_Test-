from collections import Counter

# 풀이
def solution(N, stages):
    answer = []
    value = {}
    c = Counter(stages)
    total = len(stages)
    failure = 0
    for n in range(1,N+1):
        if c[n] == 0:
            failure = 0
        else:
            failure = c[n] / total
        total = total - c[n]
        value[n] = failure
    value.items() # key, value 가 tuple로 들어있는 리스트 (dictionary 객체)로 만든다
    value_sort = sorted(value.items(), key = lambda x: x[1], reverse = True)
    # print(len(value_sort))
    for v in range(len(value_sort)):
        answer.append(value_sort[v][0])
    print(answer)
    return answer

## 다른 사람 풀이
def solution2(N, stages):
    result = {}
    denominator = len(stages)
    for stage in range(1, N+1):
        if denominator != 0:
            count = stages.count(stage) # stages에 있는 숫자의 개수를 1부터 N+1 까지 count해서 저장함
            result[stage] = count / denominator # 딕셔너리에서 1부터 N+1 까지의 key 값에 실패율에 해당하는 value를 매칭
            denominator -= count
        else:
            result[stage] = 0
    return  sorted(result, key = lambda x : result[x], reverse = True) # result[x]를 통해서 딕셔너리의 value에 접근한후, value값을 기준으로 내림차순 정렬
N = 5
stages = [2, 1, 2, 6, 2, 4, 3, 3]
solution(N, stages)
