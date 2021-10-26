class TrieNode:
    def __init__(self, char=""):
        self.childrens = {}
        self.is_end = False
        self.char = char


class Trie:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        if word is None:
            return
        word = word.lower()
        current = self.root
        for w in word:
            if w not in current.childrens:
                current.childrens[w] = TrieNode(w)
            current = current.childrens[w]
        current.is_end = True

    def search(self, word: str) -> bool:
        if word is None:
            return False
        current = self.root
        word = word.lower()

        for w in word:
            if w not in current.childrens:
                return False
            current = current.childrens[w]
        if current.is_end:
            return True
        return False

    def startsWith(self, prefix: str) -> bool:
        current = self.root
        for w in prefix:
            if w not in current.childrens:
                return False
            current = current.childrens[w]
        return True

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)