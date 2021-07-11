class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

node =[]
for i in range(0,13):
    node.append(Node(i))

# node[0].neighbors.append(node[1])
# node[0].neighbors.append(node[2])
# node[0].neighbors.append(node[3])
#
# node[1].neighbors.append(node[0])
# node[1].neighbors.append(node[4])
# node[1].neighbors.append(node[6])
#
# node[2].neighbors.append(node[0])
# node[2].neighbors.append(node[7])
#
# node[3].neighbors.append(node[0])
# node[3].neighbors.append(node[8])
# node[3].neighbors.append(node[9])
#
#
# node[4].neighbors.append(node[1])
# node[4].neighbors.append(node[6])
#
#
# node[6].neighbors.append(node[1])
# node[6].neighbors.append(node[4])
#
#
# node[7].neighbors.append(node[2])
# node[7].neighbors.append(node[8])
# node[7].neighbors.append(node[9])
#
# node[8].neighbors.append(node[3])
# node[8].neighbors.append(node[7])
# node[8].neighbors.append(node[9])
#
# node[9].neighbors.append(node[3])
# node[9].neighbors.append(node[11])
# node[9].neighbors.append(node[8])
# node[9].neighbors.append(node[7])
#
#
# node[11].neighbors.append(node[9])
# node[11].neighbors.append(node[12])
#
# node[12].neighbors.append(node[11])


node[0].neighbors.append(node[1])
node[1].neighbors.append(node[0])



class Solution:
    def cloneGraph(self, node: Node) -> Node:

        visited = set()
        new_node_key = {}
        queue = []

        head_node = None

        if not node:
            return Node


        queue.append(node)
        visited.add(node)
        new_node_key[node.val] = Node(node.val)
        head_node = new_node_key[node.val]

        while queue:
            next_node = queue.pop(0)
            print('visited',next_node.val)

            if next_node.val not in new_node_key:
                new_node_key[next_node.val] = Node(next_node.val)

            for i_node in next_node.neighbors:
                if i_node not in visited:
                    visited.add(i_node)
                    queue.append(i_node)

                if i_node.val not in new_node_key:
                    new_node_key[i_node.val] = Node(i_node.val)
                new_node_key[next_node.val].neighbors.append(new_node_key[i_node.val])


        return head_node


def bfs(node:Node):
    queue =[]
    visited = set()

    queue.append(node)
    while queue:
        next_node = queue.pop(0)

        print(next_node.val)

        for i_node in next_node.neighbors:
            if i_node not in visited:
                visited.add(i_node)
                queue.append(i_node)
Solution.cloneGraph(Solution,None)
#bfs(Solution.cloneGraph(Solution,node[0]))
