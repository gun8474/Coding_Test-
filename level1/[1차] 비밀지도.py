def solution(n, arr1, arr2):
    answer = []
    for i in range(n):
        arr_shap = ''
        bin1  = format((arr1[i]), 'b') # 리스트의 각 숫자를 이진수로 변환
        bin1 = bin1.zfill(n) # 변환된 이진수를 앞에 0을 채워서 n 만큼 길이를 맞춰줌

        bin2 = format((arr2[i]), 'b')
        bin2 = bin2.zfill(n)
        for j in range(n):
            arr = int(bin1[j]) + int(bin2[j])
            # print(arr)
            if arr == 0:
                arr_shap = arr_shap + str(' ')
            elif arr == 1 or 2:
                arr_shap = arr_shap + str("#")
        answer.append(arr_shap)
    # print(answer)
    return answer

# 다른 사람 풀이
def solution1(n, arr1, arr2):
    answer = []
    for i , j in zip(arr1,arr2):
        a12 = str(bin(i|j)[2:]) # bin의 결과에서 두개의 이진수 값을 or 연산을 통해 구하고 앞의 0b를 제외함
        a12 = a12.rjust(n,'0') # rjust()를 통해 a12를 오른쪽으로 정렬하고 n보다 길이가 작으면 앞에는 0으로 채워줌
        a12 = a12.replace('1', '#')
        a12 = a12.replace('0', ' ')
        answer.append(a12)
    print(answer)
    return answer
n = 6
arr1 = [46, 33, 33 ,22, 31, 50]
arr2 = 	[27 ,56, 19, 14, 14, 10]
solution(n , arr1, arr2)
