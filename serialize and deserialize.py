# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
#[1,2,3,null,null,4,5,6,7]

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)

root.right.left =TreeNode(4)
root.right.right =TreeNode(5)

root.right.left.left =TreeNode(6)
root.right.left.right =TreeNode(7)
class Codec:

    def serialize(self, root:TreeNode):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """

        data = []
        if not root:
            return []

        def dfs( node:TreeNode):
            print(node.val)

            data.append(node.val)

            if node.left:
                dfs(node.left)
            if node.right:
                data.append('R')
                data.append(node.val)
                dfs(node.right)

        dfs(root)
        return data

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """

        print(data)

        if len(data)==0:
            return None

        node_key ={}
        count = 0
        root = TreeNode(data[0])
        node_key[data[0]]=root
        next_node = root
        before_node = None
        for i in data[1:]:


            if i == 'R':
                count = 2
                continue

            if count==2:
                before_node = node_key[i]
                count -= 1

            elif count == 1:
                new_node = TreeNode(i)
                node_key[i] = new_node
                before_node.right = new_node
                next_node = new_node
                count -= 1
            else:
                new_node = TreeNode(i)
                node_key[i] = new_node
                next_node.left = new_node
                next_node = next_node.left



        return root


# Your Codec object will be instantiated and called as such:
ser = Codec()
deser = Codec()
ans = deser.deserialize(ser.serialize(root))