input_node = [[1,2],[2,3],[0,1],[2,4]]

node = None
discovered = []
class TreeNode:
    def __init__(self,val = 0):
        self.val = val
        self.linked_node = []

def make_tree():
    init_list = input_node.pop(0)

    root_node = TreeNode(init_list[0])
    init_node = TreeNode(init_list[1])
    root_node.linked_node.append(init_node)
    init_node.linked_node.append(root_node)

    for i_node in input_node:
        node_result_node_start = find_node(root_node,i_node[0])
        discovered.clear()
        node_result_node_end = find_node(root_node, i_node[1])
        discovered.clear()

        if node_result_node_start != None and node_result_node_end != None:
            break
        elif node_result_node_start != None and node_result_node_end == None:
            node_end = TreeNode(i_node[1])
            node_result_node_start.linked_node.append(node_end)
            node_end.linked_node.append(node_result_node_start)
        elif node_result_node_start == None and node_result_node_end != None:
            node_start = TreeNode(i_node[0])
            node_result_node_end.linked_node.append(node_start)
            node_start.linked_node.append(node_result_node_end)
        else:
            temp_i_node = i_node
            input_node.remove(i_node)
            input_node.append(temp_i_node)

    return root_node

def find_node(node:TreeNode, node_val):
    discovered.append(node.val)
    if node_val == node.val:
        return node
    else:
        for i_node in node.linked_node:
            if i_node.val not in discovered:
                temp_node =  find_node(i_node,node_val)
                if(temp_node != None and temp_node.val == node_val):
                    return temp_node

    return None

max_height = 9999
node_discovered= []
def find_node_height(i_node:TreeNode,current_height):

    i_node




node = make_tree()

node




