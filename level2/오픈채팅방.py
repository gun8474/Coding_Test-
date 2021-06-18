def solution(record):
    answer = []
    id_list = []

    for i in range(len(record)):
        id = record[i].split(' ')[1]
        id_list.append(id)
    set_id = set(id_list)
    id_list_x = list(set_id) # 중복을 제거한 아이디의 종류

    for records in record:
        for a in id_list_x:
            id_idx = [i for i, value in enumerate(id_list) if value == a]
            id_idx = sorted(id_idx, reverse=True)
            final = id_idx[0]
            if record[final].split(' ')[0] == 'Leave':
                final = id_idx[1]

            finname = record[final].split(' ')[2]

            if records.split(' ')[1] == a:
                if records.split(' ')[0] == 'Enter':
                    answer.append(finname + '님이 들어왔습니다')
                if records.split(' ')[0] == 'Leave':
                    answer.append(finname + '님이 나갔습니다')
    return answer

# 다른사람 풀이1
'''Dictionary를 통한 풀이 방법'''

def solution1(record):
    answer, tmp = list(), list()
    id_name = {'Enter': '님이 들어왔습니다.',
               'Leave': '님이 나갔습니다.'}
    temp = [string.split(' ') for string in record] # 상태와 아이디, 이름을 분할해서 하나의 리스트로 만듬

    for i in temp:
        if i[0] != 'Leave':
            id_name[i[1]] = i[2] # dictionary에 추가 (key : i[1], value : i[2])
        if i[0] == 'Enter' or i[0] == 'Leave':
            tmp.append('{},{}'.format(i[1], i[0])) # tmp = ['uid1234,Enter', 'uid4567,Enter', 'uid1234,Leave', 'uid1234,Enter']

    for i in tmp:
        a, b = i.split(',')
        answer.append('{}{}'.format(id_name[a], id_name[b]))

record =["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]
solution1(record)

