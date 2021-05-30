from typing import List

board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
word = "ABCCED"
#Back Tracking
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:

        start_group = set()

        for i in range(0,len(board)):
            for j in range(0,len(board[i])):
                if board[i][j] ==word[0]:
                    start_group.add((i,j))

        print('Find Start Group',start_group)


        def bfs(x:int,y:int, find_word:str, path:[])->bool:

            print('path',path)

            path.append([board[x][y]])

            if board[x][y] != find_word[len(path)]:
                return False

            if path == word:
                return True
            up = (x -1, y)
            down = (x+1,y)
            right = (x,y+1)
            left = (x,y-1)

            if up[0]>=0:
                if bfs(up[0],up[1],find_word,path):
                    return True

            if down[0]<=len(board)-1:
                if bfs(down[0], down[1], find_word, path):
                    return True
t
            if right[0]<=len(board[0])-1:
                if bfs(right[0], right[1], find_word, path):
                    return True

            if left[0]>=0:
                if bfs(left[0], left[1], find_word, path):
                    return True
            return False

        for node in start_group:
            print(node)
            if bfs(node[0],node[1], word,[]):
                return True

        return False

print(Solution.exist(Solution,board,word))