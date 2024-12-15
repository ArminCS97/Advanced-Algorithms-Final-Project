from search import Search


class BSTNode:
    def __init__(self, word):
        self.word = word
        self.left = None
        self.right = None


class BSTLexicographicalSearch(Search):
    def __init__(self, words):
        super().__init__(words, [])
        self.root = None

    def insert(self, word):
        if self.root is None:
            self.root = BSTNode(word)
        else:
            self._insert(self.root, word)

    def _insert(self, node, word):
        if node is None:
            return
        if word < node.word:
            if node.left is None:
                node.left = BSTNode(word)
            else:
                self._insert(node.left, word)
        else:
            if node.right is None:
                node.right = BSTNode(word)
            else:
                self._insert(node.right, word)

    def search(self, word):
        return self._search(self.root, word)

    def construct(self):
        for word in self.words:
            self.insert(word)

    def _search(self, node, word):
        """Recursive search in the OBST."""
        if node is None:
            return False  # Word not found
        if node.word == word:
            return True  # Word found
        elif word < node.word:
            return self._search(node.left, word)  # Traverse left subtree
        else:
            return self._search(node.right, word)  # Traverse right subtree

    def inorder_traversal(self):
        """Perform an in-order traversal of the tree."""
        result = []
        self._inorder_traversal(self.root, result)
        return result

    def _inorder_traversal(self, node, result):
        """Helper function for in-order traversal."""
        if node:
            self._inorder_traversal(node.left, result)
            result.append(node.word)
            self._inorder_traversal(node.right, result)
