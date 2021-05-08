from typing import List

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

    def insert(self, word: str,index:int) -> None:

        current_node = self.root_node


        for i in range(len(word) - 1, -1, -1):
            if word[i] not in current_node.next_nodes:
               new_node = TrieNode(word[i],{})
               current_node.next_nodes[word[i]]= new_node

            current_node = current_node.next_nodes[word[i]]

        current_node.next_nodes['!'] = index
        """
        Inserts a word into the trie.
        """
    def search(self, word: str) -> TrieNode:
        """
        Returns if the word is in the trie.
        """
        current_node = self.root_node

        #for i in range(len(words)-1,0,-1):
        for i in word:
            if i in current_node.next_nodes:
                current_node = current_node.next_nodes[i]
            else:
                return None

        return current_node



words = ["a",""]
words = ["bat","tab","cat"]

words = ["abcd","dcba","lls","s","sssll"]

words = ["a","abc","aba",""]

class Solution:

    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        result =[]

        trie = Trie()
        trie.__init__()
        for i in range(0,len(words)):
            trie.insert(words[i],i)

        sub_result =[]

        def bfs(node:TrieNode, path:[]):

            for i in node.next_nodes:
                if i == '!':
                    if not path or path == path[::-1] :
                        sub_result.append(node.next_nodes[i])
                        return
                    else:
                        continue
                bfs(node.next_nodes[i],path+[i])

        blank_list = []
        for i in range(0,len(words)):
            searched_node = trie.search(words[i])
            if words[i]=="":
                blank_list.append(i)

            if not searched_node:
                continue
            sub_result = []
            bfs(searched_node ,[])
            for j in sub_result:
                if i != j :
                    result.append([i,j])

        for i in range(0,len(words)):
            if i in blank_list:
                continue
            for j in blank_list:
                result.append([i,j])


        return result
print(Solution.palindromePairs(Solution,words))