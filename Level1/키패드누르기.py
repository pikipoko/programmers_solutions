def distanceCal(n1, n2):    # 상하좌우 4가지 방향으로만 이동가능
    if n1[0] < n2[0]:
        x = n2[0] - n1[0]
    else:
        x = n1[0] - n2[0]
    if n1[1] < n2[1]:
        y = n2[1] - n1[1]
    else:
        y = n1[1] - n2[1]
    return x + y
    
def solution(numbers, hand):
    answer = ''
        
    phone = [[3, 1], [0, 0], [0, 1], [0, 2], [1, 0], [1, 1], [1, 2], [2, 0], [2, 1], [2, 2], [3, 0], [3, 2]]
    """
    1 2 3   0,0 0,1 0,2
    4 5 6   1,0 1,1 1,2
    7 8 9   2,0 2,1 2,2
    * 0 #   3,0 3,1 3,2
    numbers의 수를 index로 바로 이용하기 위해 0~9를 좌표로 두었다.
    """
    left = phone[10]   # 왼손 시작점 *
    right = phone[11]  # 오른손 시작점 #
    for n in numbers:
        if n in [1, 4, 7]:
            answer += "L"
            left = phone[n]
        elif n in [3,6,9]:
            answer += "R"
            right = phone[n]
        # 중앙에 있는 숫자들만 거리계산을 하면 된다. - 2,5,8,0
        elif distanceCal(left, phone[n]) < distanceCal(right, phone[n]):
            answer += "L"
            left = phone[n]
        elif distanceCal(left, phone[n]) == distanceCal(right, phone[n]):
            if hand in "right":
                answer += "R"
                right = phone[n]
            else:
                answer += "L"
                left = phone[n]
        else:
            answer += "R"
            right = phone[n]
    
    return answer
