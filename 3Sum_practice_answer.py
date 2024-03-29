num = [-1,0,1,2,-1,-4]

def sum_3(nums):

    results = []
    nums.sort()

    for i in range(len(nums) -2):
        #중복된 값 건너뛰기
        if i > 0 and nums[i] == nums[i-1]:
            continue

        #간격을 좁혀가며 합 Sum 계산
        left, right = i +1, len(nums) -1
        while left < right:
            sum = num[i] + num[left] + num[right]

            if sum < 0 :
                left += 1
            elif sum > 0 :
                right -= 1
            else:
                #sum = 0 인 경우이므로 정답 및 스킵 처리
                temp = []
                temp.append(nums[i])
                temp.append(nums[left])
                temp.append(nums[right])

                results.append(temp)

                while left < right and nums[left] == nums[left+1]:
                    left +=1
                while left < right and nums[right] == nums[right-1]:
                    right -=1
                left +=1
                right -=1








    return results






print(sum_3(num))