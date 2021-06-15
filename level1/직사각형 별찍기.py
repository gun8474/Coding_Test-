a, b = map(int, input().strip().split(' '))
# 내 풀이
answer = ''
for i in range(b):
    for j in range(a):
        print('*', end='')
    print('') # 다음줄로 넘어가기 위해 print('') 사용

# 다른사람 풀이 1
star = '*' * a
for i in range(b):
    print(star)

# 다른사람 풀이 2
answer = ('*' * a + '\n') * b
print(answer)
