a = None
root = [4,1,6,0,2,5,7,None,None,None,3,None,None,None,8]
#Output: [30,36,21,36,35,26,15,null,null,null,33,null,null,null,8]

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def make_tree( self, node: TreeNode, node_index):
        if node_index * 2 > len(root):
            return TreeNode(root[node_index-1])

        node.left = Solution.make_tree(self, TreeNode(root[node_index * 2 -1]), node_index * 2)
        node.right = Solution.make_tree(self, TreeNode(root[node_index * 2] ), node_index * 2 + 1)

        return node

    def find_bst(self,node : TreeNode,val):
        if(node.right == None and node.left == None):
            if node.val !=None and node.val >= val:
                return node.val
            else:
                return 0

        sum = 0
        if node.val >= val:
            sum = node.val
            if (node.right != None):
                sum += Solution.find_bst(self,node.right,val)
            if (node.left != None):
                sum += Solution.find_bst(self,node.left,val)
        else:
            sum = Solution.find_bst(self,node.right,val)

        return sum
    def bstToGst(self, p_root: TreeNode) -> TreeNode:
        result=[]
        for i_root in range(len(root)):
            #result.append(Solution.find_bst(self, p_root, 6))
            if(root[i_root] != None):
                result.append(Solution.find_bst(self,p_root,root[i_root]))
            else:
                result.append(None)

        return result

root_node = Solution.make_tree(Solution,TreeNode(root[0]),1)
print(Solution.bstToGst(Solution,root_node))
