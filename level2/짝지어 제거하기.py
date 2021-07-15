def solution(s):
    answer = -1
    idx = 0
    for i in range(len(s)):
        if len(s) > 1 and idx < len(s) -1:
            if s[idx] == s[idx+1]:
                s = s.replace(s[idx],'',1)
                s = s.replace(s[idx],'',1)
                idx = 0
            else:
                idx+=1
    if s == '':
        answer = 1
    else:
        answer = 0
    return answer

# 다른사람 풀이1
def solution1(s):
    stack = []
    for i in s:
        if len(stack) == 0:
            stack.append(i)
        elif stack[-1] == i:
            stack.pop()
        else:
            stack.append(i)
    if len(stack) == 0:
        return 1
    else:
        return 0

s = 'baaddbrccr'
solution(s)

