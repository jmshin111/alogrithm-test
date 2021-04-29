from typing import List

grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]


grid = [["1","1","1"],
        ["0","1","0"],
        ["0","1","0"]]
class Solution:
    def findIsland(self,grid: List[List[str]], visited:{},i:int,j:int):
        #print(i,j)
        visited[str(i ) + str('-') + str(j)] = 'O'
        if (str(i-1 ) + str('-') + str(j)) not in visited and  i-1>=0 and grid[i-1][j]== "1":
            Solution.findIsland(Solution,grid,visited,i-1,j)

        if (str(i+1 ) + str('-') + str(j)) not in visited and i+1<=len(grid)-1 and  grid[i+1][j]== "1":
            Solution.findIsland(Solution, grid, visited, i +1, j )

        if (str(i) + str('-') + str(j-1)) not in visited  and j-1>=0 and grid[i][j-1]== "1":
            Solution.findIsland(Solution, grid, visited, i , j - 1)

        if (str(i) + str('-') + str(j+1)) not in visited and j+1<=len(grid[i])-1 and grid[i][j+1]== "1":
            Solution.findIsland(Solution, grid, visited, i, j + 1)

    def numIslands(self, grid: List[List[str]]) -> int:
        result = 0

        visited = {}

        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if str(i)+str('-')+str(j) in visited:
                    continue
                elif grid[i][j] == "1":
                    Solution.findIsland(Solution,grid,visited,i,j)
                    #print('R',result)
                    result += 1

        return result



print(Solution.numIslands(Solution,grid))
