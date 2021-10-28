from typing import List


class TrieNode:
    def __init__(self, char=""):
        self.childrens = {}
        self.is_end = False
        self.val = float("inf")
        self.char = char


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        current = self.root
        for w in word:
            if w not in current.childrens:
                current.childrens[w] = TrieNode(w)
            current = current.childrens[w]
        current.is_end = True

    def search(self, word):
        current = self.root
        res = ""
        for wd in word:
            if wd not in current.childrens:
                break
            res += wd
            current = current.childrens[wd]
            if current.is_end:
                return res
        return word


class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:

        tr = Trie()
        for d in dictionary:
            tr.insert(d)
        res = []
        for wd in sentence.split(" "):
            rest = tr.search(wd)
            res.append(rest)
        return " ".join(res)
