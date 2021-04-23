# 첫번째 방법
def solution1(participant, completion):
    for i in range(len(participant)):
        for j in range(len(completion)):
            if participant[i] == completion[j]:
                participant[i] = 0
                completion[j] = 0
                break
    for i in range(len(participant)):
        if participant[i] != 0:
            answer = participant[i]
    print(answer)
    return answer
#

# zip을 이용한 2번째 방법
def solution2(participant, completion):
    participant.sort() # 알파벳별 오름차순 정렬
    completion.sort()
    for p,c in zip(participant, completion):
        if p != c:
            return p # 참가자 중 중복되는 경우
    return participant[-1] # 참가자 중 중복되지 않는 경우

participant = ["mislav", "stanko", "mislav", "ana"]
completion = ["stanko", "ana", "mislav"]
solution1(participant,completion)
solution2(participant,completion)
