def solution(array, commands):
    answer = []
    for c in commands:
        use = array[c[0]-1:c[1]]
        use.sort()
        answer.append(use[c[2]-1])
    return answer
  
  #return list(map(lambda a: sorted(array[a[0]-1:a[1]])[a[2]-1], commands)) 한줄로 끝낼 수 있음. (다른 사람 풀이)
