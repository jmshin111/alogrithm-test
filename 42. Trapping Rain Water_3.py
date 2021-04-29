from typing import List


height = [0,1,0,2,1,0,1,3,2,1,2,1]
height = [4,2,3]




height = [0,1,0,2,1,0,1,3,2,1,2,1]
height = [2,0,2]
height = [4,2,0,3,2,5]
height = [4,2,3]
class Solution:
    def trap(self, height: List[int]) -> int:

        if(len(height)<3):
            return 0
        p1_start = 0
        p1_end = 1
        p2_start = len(height)-1
        p2_end = len(height)-2
        p1_sum = 0
        p2_sum = 0
        while height[p1_start] > height[p1_end]:
            p1_end += 1
            if(p1_end == len(height)):
                break
        if p1_end == len(height) :
            p1_sum = 0
        else:
            p1_start_height = height[p1_start]
            p1_start +=1
            while(p1_start<p1_end):
                p1_sum += p1_start_height -height[p1_start]
                p1_start += 1


        while height[p2_start] > height[p2_end]:
            p2_end -=1
            if (p2_end == -1):
                break
        if p2_end == -1:
            p2_sum = 0
        else:
            p2_start_height = height[p2_start]
            p2_start -= 1
            while (p2_start > p2_end):
                p2_sum += p2_start_height - height[p2_start]
                p2_start -= 1

        if( p1_end < p2_end):
            return p1_sum+p2_sum+ Solution.trap(Solution,height[p1_end:p2_end+1])
        elif( p1_end == p2_end):
            return p1_sum + p2_sum
        else:
            if(height[0] < height[len(height)-1]):
                return p1_sum
            else:
                return p2_sum



print(Solution.trap(Solution,height))



