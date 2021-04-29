# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

root = TreeNode(1)
root.left = TreeNode(2)

class Solution:

    max_height = -1
    min_height = 99999
    result = True

    def isBalanced(self, root: TreeNode) -> bool:
        if not root or (not root.left and not root.right):
            return True
        def dfs(node:TreeNode, height:int):

            if not Solution.result:
                return

            if not node.right and not node.left:
                Solution.max_height = max(Solution.max_height, height)
                Solution.min_height = min(Solution.min_height, height)
                print(Solution.max_height,Solution.min_height)
                if Solution.max_height - Solution.min_height >1:
                    Solution.result = False


            if node.right:
                dfs(node.right,height+1)

            if node.left:
                dfs(node.left,height+1)
        dfs(root,0)

        return Solution.result


print(Solution.isBalanced(Solution,root))