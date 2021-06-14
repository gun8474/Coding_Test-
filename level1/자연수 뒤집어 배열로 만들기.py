def solution(n):
    answer = []
    s = str(n)
    for i in range(len(s)-1,-1, -1):
        answer.append(int(s[i]))
    return answer

# 다른사람 풀이1
def solution1(n):
    arr = list(str(n)) # 자연수를 string 형태로 바꿔서 리스트로 변환
    arr.reverse() # 리스트를 reverse함
    return list(map(int, arr)) # reverse한 list를 정수로 바꿔 주기 위해 맵으로 바꿔줌

    """
    map(int, arr) --> map에 int와 리스트인 arr를 넣으면 리스트의 모든 요소를 int형으로 변환한다.
    list(int,arr) --> 그 다음 list()를 사용해서 map의 결과를 다시 리스트로 만들어준다.
    """

# 다른사람 풀이2
def solution2(n):
    return list(map(int, reversed(str(n))))

n = 1234567890
solution(n)
