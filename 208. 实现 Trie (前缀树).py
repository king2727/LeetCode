class Trie(object):

    def __init__(self):
        self.root = {}
        self.end_of_word = "#"

    def insert(self, word):
        """
        :type word: str
        :rtype: None
        """
        node = self.root
        for char in word:
            node = node.setdefault(char, dict())
        node[self.end_of_word] = self.end_of_word


    def search(self, word):
        """
        :type word: str
        :rtype: bool
        """
        node = self.root
        for char in word:
            if char not in node:
                return False
            else:
                node = node[char]
        return self.end_of_word in node


    def startsWith(self, prefix):
        """
        :type prefix: str
        :rtype: bool
        """
        node = self.root
        for char in prefix:
            if char not in node:
                return False
            else:
                node = node[char]
        return True




# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)