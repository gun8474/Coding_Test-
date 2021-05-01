def solution(d, budget):
    answer = 0
    d.sort()
    ds = 0
    for i in range(len(d)):
        if ds + d[i] <= budget:
            ds = ds + d[i]
            answer +=1
    print(answer)
    return answer
# d= [2,2,2,3]
# budget = 10
# solution(d, budget)
