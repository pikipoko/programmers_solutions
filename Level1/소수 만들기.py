def solution(nums):
    answer = 0
    # 소수는 1과 자신으로만 나눠 떨어지는 수
    i1,i2,i3 = 0,1,2
    
    while i1 < len(nums)-2:        
        i2 = i1 + 1
        while i2 < len(nums)-1:
            i3 = i2 + 1            
            while i3 < len(nums):                
                num = nums[i1] + nums[i2] + nums[i3]
                i = 2
                while i < num:
                    if num % i == 0:                       
                        break
                    i += 1
                if num == i:                    
                    answer += 1                
                i3 +=1
            i2 += 1
        i1 += 1
    return answer
