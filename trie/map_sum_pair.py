class TrieNode:
    def __init__(self, char=""):
        self.childrens = {}
        self.is_end = False
        self.val = 0
        self.char = char


class MapSum:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, key: str, val: int) -> None:
        current = self.root
        for w in key:
            if w not in current.childrens:
                current.childrens[w] = TrieNode(w)
            current = current.childrens[w]
        current.is_end = True
        current.val = val

    def sum(self, prefix: str) -> int:

        current = self.root
        for w in prefix:
            if w in current.childrens:
                current = current.childrens[w]
            else:
                return 0

        def dfs(node):
            summ = 0
            for c in node.childrens.keys():
                summ += dfs(node.childrens[c])
            return summ + node.val

        return dfs(current)
# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)