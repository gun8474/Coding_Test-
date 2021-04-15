import numpy

def solution(board, moves):
    answer = 0
    basket = []

    board = numpy.array(board)

    row = board.shape[0]
    column = board.shape[1]

    for i in range(row):
        for j in range(column):
            if board[j][i] != 0:
                basket.append(board[j][i])
                if len(basket) < 2:
                    break
                else:
                    if basket[-1] == basket[-2]:
                        basket.pop(-1)
                        basket.pop(-1)
                        answer = answer + 2
    print(answer)
    return answer
moves = [1,5,3,5,1,2,1,4]
board = [[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]]
a = solution(board, moves)
a

