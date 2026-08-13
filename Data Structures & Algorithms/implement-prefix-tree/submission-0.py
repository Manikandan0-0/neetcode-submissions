class TrieNode:
    def __init__(self):
        self.tree={}
        self.end=False
class PrefixTree:

    def __init__(self):
        self.root=TrieNode()        

    def insert(self, word: str) -> None:
        curr=self.root
        for c in word:
            if c not in curr.tree:
                curr.tree[c]=TrieNode()
            curr=curr.tree[c]
        curr.end=True


    def search(self, word: str) -> bool:
        curr=self.root
        for c in word:
            if c not in curr.tree:
                return False
            curr = curr.tree[c]
        return curr.end

    def startsWith(self, prefix: str) -> bool:
        curr=self.root
        for c in prefix:
            if c not in curr.tree:
                return False
            curr=curr.tree[c]
        return True
        
        