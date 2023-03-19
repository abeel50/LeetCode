class TrieNode:
    def __init__(self):
        self.isEnd =  False
        self.children = {}
        
class WordDictionary:

    def __init__(self):
         self.root = TrieNode()

    def addWord(self, word: str) -> None:
        pCrawl = self.root
        
        for c in word:
            if c not in pCrawl.children:
                pCrawl.children[c] = TrieNode()
            pCrawl = pCrawl.children[c]
            
        pCrawl.isEnd = True
    

    def search(self, word: str) -> bool:
        
        def dfs(j, root):
            pCrawl = root

            for i in range(j, len(word)):
                c = word[i]

                if c  == ".":
                    for child in pCrawl.children.values():
                        if child and dfs(i + 1, child):
                            return True
                    return False
                    
                else:
                    if c not in pCrawl.children:
                        return False
                    pCrawl = pCrawl.children[c]
            return pCrawl.isEnd
        return dfs(0, self.root)

                

# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)