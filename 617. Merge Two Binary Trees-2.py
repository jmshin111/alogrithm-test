# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:

    def mergeTrees(self, root1: TreeNode, root2: TreeNode) -> TreeNode:

        def dfs(root1: TreeNode, root2: TreeNode):

            root1.val += root2.val
            if root1.left and root2.left:
                dfs(root1.left,root2.left)
            elif not root1.left and root2.left:
                root1.left = root2.left

            if root1.right and root2.right:
                dfs(root1.right, root2.right)
            elif not root1.right and root2.right:
                root1.right = root2.right
        if root1 and root2:
            dfs(root1,root2)
            return root1
        elif root1:
            return root1
        elif root2:
            return root2
