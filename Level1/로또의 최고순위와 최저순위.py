def solution(lottos, win_nums):
    answer = [6,6] # 0에는 최고 순위, 1에는 최저 순위

    for l in lottos:
        if l in win_nums:
            answer[0] -= 1
            answer[1] -= 1
        elif l == 0:
            answer[0] -= 1
    if answer[0] != 6:
        answer[0] += 1
    if answer[1] != 6:
        answer[1] += 1
        
    return answer
