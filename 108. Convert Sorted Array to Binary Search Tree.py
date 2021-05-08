
# Definition for a binary tree node.
from typing import List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
nums = [-10, -3, 0, 5, 9]
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:


        print(nums)

        def bfs(start_index,end_index )->TreeNode:

            if end_index == start_index:
                return TreeNode(nums[start_index])

            middle_index =int((start_index+end_index)/2)

            middle_tree = TreeNode(nums[middle_index])

            if middle_index -1 >=start_index:
                middle_tree.left = bfs(start_index, middle_index-1)

            if middle_index + 1 <= end_index:
                middle_tree.right = bfs(middle_index+1, end_index )

            return middle_tree

        return bfs(0,len(nums)-1)





tree =  Solution.sortedArrayToBST(Solution,nums)
print(tree.val)