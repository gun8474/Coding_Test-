def solution(array, commands):
    answer = []
    for s in commands:
        i = s[0]
        j = s[1]
        k = s[2]

        new_ar = array[i-1:j]
        new_ar.sort()
        answer.append(new_ar[k-1])
    return answer

array = [1, 5, 2, 6, 3, 7, 4]
commands = [[2, 5, 3], [4, 4, 1], [1, 7, 3]]
solution(array, commands)


