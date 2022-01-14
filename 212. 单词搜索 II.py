from collections import defaultdict

class Trie():
    def __init__(self):
        self.children = defaultdict(Trie)
        self.word = ""
        self.is_word = False

    def insert(self, word):
        node = self
        for char in word:
            node = node.children[char]
        node.is_word = True
        node.word = word

class Solution(object):
    def __init__(self):
        self.results = set()
        self.directs = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    def findWords(self, board, words):
        """
        :type board: List[List[str]]
        :type words: List[str]
        :rtype: List[str]
        """
        trie = Trie()
        for word in words:
            trie.insert(word)

        m = len(board)
        n = len(board[0])

        mark = [[0 for _ in range(n)] for _ in range(m)]

        for i in range(m):
            for j in range(n):
                self.dfs(trie, i, j, board, mark)

        return list(self.results)



    def dfs(self, now, i, j, board, mark):
        if board[i][j] not in now.children:
            return

        ch = board[i][j]
        now = now.children[ch]
        if now.is_word:
            self.results.add(now.word)

        mark[i][j] = 1
        for direct in self.directs:
            cur_i = i + direct[0]
            cur_j = j + direct[1]
            if 0 <= cur_i < len(board) and 0 <= cur_j < len(board[0]) and mark[cur_i][cur_j] == 0:
                self.dfs(now, cur_i, cur_j, board, mark)

        mark[i][j] = 0


board = [["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]]
words = ["oath","pea","eat","rain"]

test = Solution()
test.findWords(board, words)
print(test.results)