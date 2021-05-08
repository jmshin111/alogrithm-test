# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


from typing import List

preorder = [3,9,20,15,7]
inorder = [9,3,15,20,7]


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:


        def makeTree(node:TreeNode, inorder: List[int]  )->TreeNode:
            middle_index = -1
            if not inorder:
                return node

            for i in range(0,len(inorder)):
                if inorder[i]== node.val:
                    middle_index = i
                    break

            if preorder:
                next_val = preorder[0]
                for i in range(0, middle_index):
                    if next_val == inorder[i]:
                        preorder.pop(0)
                        node.left = makeTree( TreeNode(next_val), inorder[:middle_index])
                        break

            else:
                return node

            if preorder:
                next_val = preorder[0]
                for i in range(middle_index+1, len(inorder)):
                    if next_val == inorder[i]:
                        preorder.pop(0)
                        node.right = makeTree( TreeNode(next_val), inorder[middle_index+1:])
                        break
            else:
                return node

            return node

        if preorder:
            root = TreeNode(preorder.pop(0))
            return makeTree(root,inorder)

        else:
            return None



root = Solution.buildTree(Solution,preorder,inorder)
root.val