class TrieNode:
    def __init__(self):
        self.word = False
        self.children = collections.defaultdict(TrieNode)        

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        root = self.root
        for c in word:
            root = root.children[c]
        root.word = True

    def search(self, word: str) -> bool:
        def dfs(root, word):
            if not word:
                return root.word
            
            if word[0] != '.':
                if word[0] in root.children:
                    return dfs(root.children[word[0]], word[1:])        
                else:
                    return False
            else:
                gotWord = False
                for k in root.children.keys():
                    gotWord |= dfs(root.children[k], word[1:])
                return gotWord
        
        return dfs(self.root, word)


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)