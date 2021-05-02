def solution(arr, divisor):
    answer = []
    for i in range(len(arr)):
        if arr[i] % divisor == 0:
            answer.append(arr[i])
    if len(answer) == 0:
       answer.append(-1)
    answer.sort()
    return answer

arr = [5, 9, 7, 10]
divisor = 5
solution(arr, divisor)
