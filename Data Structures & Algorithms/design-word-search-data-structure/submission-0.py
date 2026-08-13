class TrieNode:
    def __init__(self):
        self.tree={}
        self.end=False
class WordDictionary:

    def __init__(self):
        self.root=TrieNode()
    def addWord(self, word: str) -> None:
        curr=self.root
        for c in word:
            if c not in curr.tree:
                curr.tree[c]=TrieNode()
            curr=curr.tree[c]
        curr.end=True

    def search(self, word: str) -> bool:
        def dfs(j,root):
            curr=root
            for i in range(j,len(word)):
                c=word[i]
                if c =='.':
                    for child in curr.tree.values():
                        if dfs(i+1,child):
                            return True
                    return False
                else:
                    if c not in curr.tree:
                        return False
                    curr=curr.tree[c]
            return curr.end
        return dfs(0,self.root)
        
