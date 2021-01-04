import collections

test_root = [16,14,10,8,7,9,3,2,4,1,'#','#','#']


class TreeNode:

    def __init__(self,val = 0):
        self.val = val
        self.left_node = None
        self.right_node = None



root_node = TreeNode(16)
root_node.left_node = TreeNode(14)
root_node.right_node = TreeNode(10)
#root_node.left_node.left_node = TreeNode(8)
root_node.left_node.right_node = TreeNode(7)
root_node.left_node.right_node.left_node = TreeNode(1)
#root_node.left_node.left_node.left_node = TreeNode(2)
#root_node.left_node.left_node.right_node = TreeNode(4)
root_node.right_node.left_node = TreeNode(9)
root_node.right_node.right_node = TreeNode(3)

result =[]
def bfs_serialize(input_node:TreeNode):
    queue = collections.deque([input_node])
    result.append(input_node.val)
    while(queue):
        current_node = queue.popleft()
        print(current_node.val)

#        if(not current_node.left_node and not current_node.right_node):
#            continue

        if (current_node.left_node):
            result.append(current_node.left_node.val)
            queue.append(current_node.left_node)
        else:
            result.append('#')
        if (current_node.right_node):
            result.append(current_node.right_node.val)
            queue.append(current_node.right_node)
        else:
            result.append('#')

def bfs_deserialize(input_result:[]):
    result_node : TreeNode
    result_node = TreeNode(input_result[0])
    queue = collections.deque([result_node])

    print("==== deserialize started ====")
    print( str(input_result[0]) + " is inserted to queue")

    index = 1

    while(queue):
        current_node = queue.popleft()

        if(input_result[index] != '#'):
            print(" Inseted queue and make left node Tree "+str(input_result[index]))
            left_node = TreeNode(input_result[index])
            queue.append(left_node)
            current_node.left_node = left_node

        index += 1

        if (input_result[index] != '#'):
            print(" Inseted queue and make right node Tree " + str(input_result[index]))
            right_node = TreeNode(input_result[index])
            queue.append(right_node)
            current_node.right_node = right_node

        index += 1

    return result_node

def bfs_scan(node:TreeNode):
    print(node.val)

    queue = collections.deque([node])

    while(queue):

        current_node = queue.popleft()
        if (current_node.left_node):
            print(current_node.left_node.val)
            queue.append(current_node.left_node)
        else:
            print('#')

        if (current_node.right_node):
            print(current_node.right_node.val)
            queue.append(current_node.right_node)
        else:
            print('#')








bfs_serialize(root_node)
print(result)

bfs_scan(bfs_deserialize(result))


