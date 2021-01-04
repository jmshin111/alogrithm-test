# tree의 크기 학인 root기준으로 왼쪽 오른쪽이 최대 몇까지 있는지 알 필요가 없음
# 현재 root 기준으로 왼쪽 오른쪽 얼마인지 확인해 보기 root기준으로 마지막 node가 +1 -1 위치에 있는 것은 root와의 차이를 구하기
# 
#

# Definition for a binary tree node.

root = [4,1,6,0,2,5,7,None,None,None,3,None,None,None,8]

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:

    minimum = 99999999

    def make_tree(self, node: TreeNode, node_index):
        if node_index * 2 > len(root):
            if(root[node_index - 1]):
                return TreeNode(root[node_index - 1])
            else:
                return None

        node.left = Solution.make_tree(self, TreeNode(root[node_index * 2 - 1]), node_index * 2)
        node.right = Solution.make_tree(self, TreeNode(root[node_index * 2]), node_index * 2 + 1)

        return node

    def scan_node_dfs(self, node:TreeNode) :

        Solution.minimum = min(Solution.find_minimum_difference(self,node,node.val), Solution.minimum)
        # if(Solution.minimum ==1 ):
        #     return

        if node.left != None:
            Solution.minimum = min(abs(node.val-node.left.val), Solution.minimum)
            # if (Solution.minimum == 1):
            #     return
            Solution.scan_node_dfs(self,node.left)

        if node.right != None:
            Solution.minimum = min(abs(node.val - node.right.val), Solution.minimum)
            # if (Solution.minimum == 1):
            #     return
            Solution.scan_node_dfs(self,node.right)

        # if Solution.minimum == 1:
        #     print("=== founded 1 ===")
        #     return 1

        #print("=== node " + node.val +" is complegted")


    def find_minimum_difference(self,node:TreeNode,root_val) -> int:

        minimum_root_val = 9999999

        if node.left:
            temp_node = node.left
            while(node.right):
                if(not temp_node.right):
                    break
                temp_node = temp_node.right
            minimum_root_val = min(minimum_root_val, abs(root_val-temp_node.val))
        # else:
        #     minimum_root_val = min(minimum_root_val,abs(root_val-node.val))

        if node.right:
            temp_node = node.right

            while(node.left):
                if(not temp_node.left):
                    break
                temp_node = temp_node.left

            minimum_root_val = min(minimum_root_val, abs(root_val-temp_node.val))
        # else:
        #     minimum_root_val = min(minimum_root_val,abs(root_val-node.val))

        return minimum_root_val

    def minDiffInBST(self, root: TreeNode) -> int:

        Solution.scan_node_dfs(self,root)
        return 1

root_node = Solution.make_tree(Solution,TreeNode(root[0]),1)

Solution.scan_node_dfs(Solution,root_node)
print(Solution.minimum)

