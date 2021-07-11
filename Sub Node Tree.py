class Node:

    def __init__(self,val):
        self.val = val
        self.node_list = []

node = Node(1)

node2 = Node(2)
node.node_list.append(node2)
node.node_list.append(Node(3))
node4 = Node(4)
node.node_list.append(node4)
node4.node_list.append(Node(11))
node4.node_list.append(Node(12))
node4.node_list.append(Node(13))



node6 = Node(6)
node2.node_list.append(Node(5))
node2.node_list.append(node6)
node2.node_list.append(Node(7))
node6.node_list.append(Node(8))
node6.node_list.append(Node(9))
node6.node_list.append(Node(10))


secondNode = Node(4)
secondNode.node_list.append(Node(11))
secondNode.node_list.append(Node(12))
secondNode.node_list.append(Node(13))


class Soultion:

    result = False
    tree_visited_list = []
    tree2_visited_list = []

    def dfs(self,node:Node,visited:[]):
        visited.append(node.val)
        for i in node.node_list:
            self.dfs(self, i,visited)

    def findSubTreeUsingDfs(self,node:Node):
        current_idx = len(self.tree_visited_list)
        self.tree_visited_list.append(node.val)
        print('Tree1 visited',node.val, self.tree_visited_list[current_idx:], current_idx)
        for i_node in node.node_list:
            if not self.result:
                self.findSubTreeUsingDfs(self,i_node)

        if len(self.tree_visited_list[current_idx:])== len(self.tree2_visited_list):
            matach= True
            for i in range(0,len(self.tree2_visited_list)):
                if self.tree_visited_list[current_idx+i] != self.tree2_visited_list[i]:
                    matach = False
                    break
            if matach:
                self.result = True

        if len(self.tree_visited_list[current_idx:]) >= len(self.tree2_visited_list):
            self.tree_visited_list = self.tree_visited_list[:current_idx]

    def findSubNode(self,tree1:Node,tree2:Node)->bool:

        result = False
        self.dfs(self,tree2,self.tree2_visited_list)
        print('Tree 2 Path ',self.tree2_visited_list)
        self.findSubTreeUsingDfs(self,tree1)
        return self.result


print(Soultion.findSubNode(Soultion,node,secondNode))
