def solution(numbers):
    answer = []

    for i in range(len(numbers)):
        for j in range(len(numbers) - i-1):
            sum = numbers[i] + numbers[len(numbers)-j-1]
            answer.append(sum)
            # print(4-i)
    return answer

a = solution([2,1,3,4,1])
new_list=[]

#  중복제거 및 오름차순 정렬
for v in a:
    if v not in new_list:
        new_list.append(v)
        new_list.sort()
print(new_list)

