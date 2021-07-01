def solution(new_id):     
    ok = "abcdefghijklmnopqrstuvwxyz1234567890-_."

    #1단계
    answer = new_id.lower()

    #2단계    
    c=0
    for i,a in enumerate(answer):
        if a not in ok:
            answer = answer[:i-c] + answer[i-c+1:]
            c += 1        
    
    #3단계
    dotstart = answer.find(".")
    dotend = answer.find(".")    
    c=0
    for i,a in enumerate(answer):
        if a == '.':            
            dotend = i
            if dotend - dotstart > 0:                
                answer = answer[:dotstart-c] + answer[dotend-c:]                
                c += 1                
                dotstart = dotend
        else:
            dotstart = i + 1
            dotend = i     
    
    #4단계            
    if len(answer) > 0:        
        if answer[0] == '.':
            answer = answer[1:]
        if len(answer) > 1 and answer[-1] =='.':
            answer = answer[:-1]    

    #5단계
    if answer == '':
        answer += ('a')

    #6단계
    if len(answer) > 15:        
        answer = answer[:15]
        if answer[-1] == '.':
            answer = answer[:-1]

    #7단계
    while len(answer) < 3:
        answer += answer[-1]

    print(answer)
    return answer
