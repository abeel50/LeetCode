class TrieNode:
    def __init__(self):
        self.isEnd =  False
        self.children = dict.fromkeys(string.ascii_lowercase, None)
        
        
class Trie:

    def __init__(self):
        self.root = TrieNode()
        

    def insert(self, word: str) -> None:
        pCrawl = self.root
        
        for l in range(len(word)):
            key = word[l]
            if not pCrawl.children[key]:
                pCrawl.children[key] = TrieNode()
            pCrawl = pCrawl.children[key]
            
        pCrawl.isEnd = True

    def search(self, word: str) -> bool:
        pCrawl = self.root
        for l in range(len(word)):
            key = word[l]
            if not pCrawl.children[key]:
                return False
            pCrawl = pCrawl.children[key]
            
        return pCrawl.isEnd
        

    def startsWith(self, prefix: str) -> bool:
        pCrawl = self.root
        for l in range(len(prefix)):
            key = prefix[l]
            if not pCrawl.children[key]:
                return False
            pCrawl = pCrawl.children[key]
            
        return True
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)