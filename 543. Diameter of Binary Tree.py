# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

root = TreeNode(1)
root.left = TreeNode(2)
# root.left.left = TreeNode(4)
# root.left.right = TreeNode(5)
# root.right = TreeNode(3)


class Solution:
    diameter = 0
    def diameterOfBinaryTree(self, root: TreeNode) -> int:

        self.diameter = 0

        def bfs(node:TreeNode)->int:

            left_node_depth = 0
            if node.left:
                left_node_depth =bfs(node.left)+1


            right_node_depth = 0
            if node.right:
                right_node_depth = bfs(node.right)+1

            self.diameter = max( self.diameter,left_node_depth+right_node_depth)

            return max(left_node_depth,right_node_depth)

        bfs(root)

        return self.diameter

print(Solution.diameterOfBinaryTree(Solution,root))

