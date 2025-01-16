class TrieNode:
    def __init__(self) :
        self.children = {}
        self.is_leaf = False 

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        curr = self.root 
        for letter in word :
            if letter not in curr.children :
                curr.children[letter] = TrieNode()
            curr = curr.children[letter]
        curr.is_leaf = True 

    def startsWith(self, prefix: str, status= False) -> bool:
        curr = self.root 
        for letter in prefix :
            if letter not in curr.children :
                return False 
            curr = curr.children[letter]
        return True if not status else curr.is_leaf

    def search(self, word: str) -> bool:
        return self.startsWith(word, status= True)