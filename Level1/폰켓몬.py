def solution(nums):
    answer = 0

    nums.sort()
    n = 0

    for p in nums:
        if answer >= len(nums)/2:
            break
        elif n != p:
            answer += 1
            print(n, answer)
            n = p


    return answer
