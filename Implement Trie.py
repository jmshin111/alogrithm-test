import string


class TreeNode:
    def __init__(self,val = 0):
        self.val = val
        self.linked_node = []


class Trie:
    def __init__(self):
        self.root_trie = TreeNode(None)

    def insert(self, input_str : string):
        currnet_node = self.root_trie
        matched_yn = False

        for i in range(len(input_str)):
            for i_node in currnet_node.linked_node:
                if( input_str[i] == i_node.val ):
                    currnet_node = i_node
                    matched_yn = True
                    break

            if(matched_yn):
                matched_yn = False
                continue
            else:
                new_node = TreeNode(input_str[i])
                currnet_node.linked_node.append(new_node)
                currnet_node = new_node




        print(input_str+" is competed")

    def search(self,input_str : string):
        current_node = self.root_trie

        for i in range(len(input_str)):
            for i_node in current_node.linked_node:
                if (input_str[i] == i_node.val):
                    current_node = i_node
                    matched_yn = True
                    break

            if (matched_yn):
                matched_yn = False
                continue
            else:
                return False
        return True

    def startWith(self,input_str : string):

        current_node = self.root_trie

        for i in range(len(input_str)):
            for i_node in current_node.linked_node:
                if (input_str[i] == i_node.val):
                    current_node = i_node
                    matched_yn = True
                    break

            if (matched_yn):
                matched_yn = False
                continue
            else:
                return False
        return True

trie = Trie()

trie.insert('apple')
print(trie.search('apple'))
trie.insert('app')

print(trie.root_trie)