from typing import List

#inorder = [3,9,20,15,7] #NLR
#postorder = [9,3,15,20,7] #LNR

inorder = [1,2,4,5,3,6,7,9,8] #NLR
postorder = [4,2,5,1,7,9,6,8,3] #LNR


    # 가운데 거 하나를 고른다
    # NLR에서 N인지 R인지 알기 위해서 하나 고른 가운데거 다음에 오는 수가 LNR에서 가운데 수보다 더 왼쪽에 있는지 확인한다
    # 왼쪽에 있을 경우 가운데 노드의 왼쪽 노드를 해당 노드를 추가한다
    # 그 다음 수는
    
   # 각 노드의 연결될 부분이 없는 Node는 X를 붙인다
   # inorder list가 모두 없고 각 Node에 X가 없을 때까지 계속 돌면서 체크한다.
   # 각 노드의 채워질 수있는 조건을 모두 만족할 때 Node연결 한다. 연결 조건은 LNR 이요


#Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:

        init_node = TreeNode(inorder.pop(0))

        def find_node(node:TreeNode,new_val):
            node_val_index_nlr = postorder.index(node.val)
            new_val_index_nlr = postorder.index(new_val)

            if node_val_index_nlr > new_val_index_nlr:
                if node.left == None:
                    new_node = TreeNode(new_val)
                    node.left = new_node
                    return
                else:
                    find_node(node.left,new_val)
            else:
                if node.right == None:
                    new_node = TreeNode(new_val)
                    node.right = new_node
                    return
                else:
                    find_node(node.right,new_val)


        while( len(inorder) !=0):
            next_node_val = inorder.pop(0)
            find_node(init_node,next_node_val)

        return init_node

node = Solution.buildTree( Solution,inorder, postorder)
print(node)