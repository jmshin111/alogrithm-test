import collections
from typing import List

g = [1,2,3]
s = [3]
class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()

        print(g)
        print(s)

        sum = 0
        len_g = len(g)

        if( len(g)== 0 or len(s)== 0):
            return 0
        for i in range(len_g):
            if(s):
                if(g[-1] <= s[-1]):
                    sum += 1
                    g.pop()
                    s.pop()
                else:
                    g.pop()



        return sum



print(Solution.findContentChildren(Solution,g,s))
