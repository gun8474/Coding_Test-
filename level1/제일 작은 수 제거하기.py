def solution(arr):
    min = arr[0]
    for i in range(1, len(arr)):
        if min > arr[i]:
            min = arr[i]
    index = arr.index(min) # index() : 배열에서 인덱스를 구함
    del arr[index]
    if len(arr) == 0:
        arr.append(-1)
    print(arr)
    return arr

# 다른사람 풀이
def solution1(arr):
    if len(arr)>1:
        arr.pop(arr.index(min(arr)))
        return arr
    else:
        return [-1]

'''
index() : 리스트에서 원하는 숫자의 인덱스를 반환 
            ex ) arr.index(1) # arr배열에서 1의 인덱스를 반환 -> 1 : 배열의 요소
pop() : 리스트에서 해당 인덱스에 해당하는 값 제거
            ex) arr.pop(3)  # arr배열에서 3번째 인덱스의 값 제거'''
arr = [4,2,8,3,6]
solution(arr)
