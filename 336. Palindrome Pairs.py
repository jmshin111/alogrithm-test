from typing import List

words = ["abcd","dcba","lls","s","sssll"]
words = ["bat","tab","cat"]
words = ["a",""]
words = ["a","abc","aba",""]



words = ["abcd","dcba","lls","s","sssll"]
words = ["a","b","c","ab","ac","aa"]
words = ["ab","ba","abc","cba"]
#[[3,0],[1,3],[4,0],[2,4],[5,0],[0,5]]
class TrieNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next_nodes = next

class Trie:

    root_node = None
    reverse_root_node = None

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

        if word =="":
            return None

        #for i in range(len(words)-1,0,-1):


        for i in word:
            if i in current_node.next_nodes:
                current_node = current_node.next_nodes[i]
            else:
                return None

        return current_node
    def searchLast(self, word: str) -> List:
        """
        Returns if the word is in the trie.
        """
        current_node = self.root_node

        result =[]
        if word =="":
            return result

        for i in range(0,len(word)-1):

            if word[i] in current_node.next_nodes:
                current_node = current_node.next_nodes[word[i]]
                if '!' in current_node.next_nodes:
                    end_index = current_node.next_nodes['!']
                    result.append([end_index,i])
            else:
                return result

        return result
class Solution:

    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        result =[]

        trie = Trie()
        trie.__init__()
        for i in range(0,len(words)):
            trie.insert(words[i],i)

        blank_index = -1

        if "" in words:
            blank_index = words.index("")

        sub_result =[]

        def bfs(node:TrieNode, path:[]):

            for i in node.next_nodes:
                if i == '!':
                    if not path or path == path[::-1] :
                        sub_result.append(node.next_nodes[i])
                    continue

                bfs(node.next_nodes[i],path+[i])

        blank_list = []
        for i in range(0,len(words)):
            if blank_index >= 0:
                if i != blank_index and  words[i] == words[i][::-1]:
                    result.append([i,blank_index])
                    result.append([blank_index,i])

            searched_node = trie.search(words[i])

            if searched_node:
                sub_result = []
                bfs(searched_node, [])
                for j in sub_result:
                    if i != j:
                        result.append([i,j])
            searched_list =  trie.searchLast(words[i])

            for i_list in searched_list:
                start_point = i_list[1]+1
                if start_point <=len(words[i]):
                    if words[i][start_point:] == words[i][start_point:][::-1]:
                        result.append([i,i_list[0]])


        return result

print(Solution.palindromePairs(Solution,words))