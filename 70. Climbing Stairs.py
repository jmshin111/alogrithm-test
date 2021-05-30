import collections



n = 7


n = 1 # 1

n= 3 #3

n =2 # 2
n =5 # 8

n = 1 # 1

n= 3 #3
n =6
class Solution:
    memory_chache ={}

    def climbStairs(self, n: int) -> int:
        if n in self.memory_chache:

            return self.memory_chache[n]

        elif n == 0:
            self.memory_chache[0] = 1
            return 1
        elif n == 1:
            self.memory_chache[1] = 1
            return 1

        else:
            self.memory_chache[n-1] = self.climbStairs(self,n - 1)
            self.memory_chache[n-2] = self.climbStairs(self,n - 2)

            return self.memory_chache[n-1] + self.memory_chache[n-2]
print(Solution.climbStairs(Solution,n))