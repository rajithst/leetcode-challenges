from typing import List


class Node:
    def __init__(self, char):
        self.char = char
        self.childrens = {}
        self.is_end = False


class Solution:
    def indexPairs(self, text: str, words: List[str]) -> List[List[int]]:

        root = Node(None)

        for word in words:
            temp = root
            for char in word:
                if char not in temp.childrens:
                    temp.childrens[char] = Node(char)
                temp = temp.childrens[char]
            temp.is_end = True

        result = []

        def search(startindex, text, trie):
            temp = root
            for i in range(startindex, len(text)):
                char = text[i]
                if char not in temp.childrens:
                    return
                temp = temp.childrens[char]
                if temp.is_end:
                    result.append([startindex, i])

        for i in range(len(text)):
            search(i, text, root)
        return result