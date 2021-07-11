def solution(board, moves):
    answer = 0
    basket = list()
    c = -1
    for m in moves:
        for i, b in enumerate(board):
            if b[m-1] != 0:
                basket.append(b[m-1])
                board[i][m-1] = 0
                c += 1
                if c > 0:
                    if basket[c-1] == basket[c]:
                        answer += 2                        
                        del basket[c-1]
                        del basket[c-1]
                        c -= 2
                break
    return answer
