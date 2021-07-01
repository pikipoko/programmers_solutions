def solution(answers):
    answer = [0,0,0]
    a1 = list()
    a2 = list()
    a3 = list()
    an = list()
    i = 0
    while i < len(answers):
        a1.append(i%5 + 1)

        if i%2 == 0:
            a2.append(2)
        else:
            if i%8 == 1:
                a2.append(1)
            if i%8 == 3:
                a2.append(3)
            if i%8 == 5:
                a2.append(4)
            if i%8 == 7:
                a2.append(5)

        if i%10 < 2:
            a3.append(3)
        elif 2 <= i%10 < 4:
            a3.append(1)
        elif 4 <= i%10 < 6:
            a3.append(2)
        elif 6 <= i%10 < 8:
            a3.append(4)
        elif 8 <= i%10 < 10:
            a3.append(5)
        i += 1

    for i, a in enumerate(answers):
        if a1[i] == a:
            answer[0] += 1
        if a2[i] == a:
            answer[1] += 1
        if a3[i] == a:
            answer[2] += 1

    m = max(answer[0],answer[1],answer[2])

    for i, a in enumerate(answer):
        if m == a:
            an.append(i+1)

    return an
