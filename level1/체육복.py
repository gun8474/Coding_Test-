def solution(n, lost, reserve):
    answer = 0

    for j in reserve:
        a = j+1
        b = j-1
        if a in lost:
            lost.remove(a)
        elif b in lost:
            lost.remove(b)

    answer = n - len(lost)
    print(answer)
    return answer

# 다른 사람 풀이 1 --> set 자료형(중복을 허용하지 않는 자료형) 사용
                    # set의 특징은 '-' 기호를 사용해서 차집합을 수행할 수 있다. (list 자료형은 '-'와 같은 차집합 연산을 할 수 없다)
def solution1(n, lost, reserve):
    set_reserve = set(reserve) - set(lost)
    set_lost = set(lost) - set(reserve)
    for i in set_reserve:
        if i-1 in set_lost:
            set_lost.remove(i-1)
        elif i+1 in set_lost:
            set_lost.remove(i+1)
    return n - len(set_lost)

# 다른 사람 풀이 2
def solution2(n, lost, reserve):
    answer = 0
    # reserve2 = [r for r in reserve if r not in lost]
    # lost2 = [l for l in lost if l not in reserve]
    for r in reserve:
        if r-1 in lost:
            lost.remove(r-1)
        elif r+1 in lost:
            lost.remove(r+1)
    answer = n-len(lost)
    print(answer)
    return answer
n = 5
lost = [2,4]
reserve = [1,3,5]
solution2(n,lost,reserve)
