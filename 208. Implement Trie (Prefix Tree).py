class TrieNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next_nodes = next

class Trie:

    root_node = None

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root_node = TrieNode('*',{})

    def insert(self, word: str) -> None:

        current_node = self.root_node

        for i in word:
            if i not in current_node.next_nodes:
               new_node = TrieNode(i,{})
               current_node.next_nodes[i]= new_node

            current_node = current_node.next_nodes[i]

        current_node.next_nodes['!'] = None
        """
        Inserts a word into the trie.
        """

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        current_node = self.root_node

        for i in word:
            if i in current_node.next_nodes:
                current_node = current_node.next_nodes[i]

            else:

                return False

        if '!' in  current_node.next_nodes:
            return True
        else:
            return False

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        current_node = self.root_node

        for i in prefix:
            if i in current_node.next_nodes:
                current_node = current_node.next_nodes[i]
            else:
                return False
        return True

# Your Trie object will be instantiated and called as such:
obj = Trie()
obj.insert('apple')
param = obj.search('apple')
print(param)
param = obj.search('app')
print(param)
param = obj.startsWith('app')
print(param)
obj.insert('app')
param = obj.search('app')
print(param)
["Trie","insert","search","search","startsWith","insert","search"]
[[],["apple"],["apple"],["app"],["app"],["app"],["app"]]