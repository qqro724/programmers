####틀린문제
##########코드 수정

# def solution(board, k):
#     answer = 0
#     return sum(board[k])

def solution(board, k):
    total = 0
    for i in range(len(board)):
        for j in range(len(board[0])):
            if i + j <= k:
                total += board[i][j]
    return total
