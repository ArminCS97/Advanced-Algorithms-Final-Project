from search import Search


class BSTNode:
    def __init__(self, word, frequency):
        self.word = word
        self.frequency = frequency
        self.left = None
        self.right = None


class BSTFrequencySearch(Search):
    def __init__(self, words, frequencies):
        super().__init__(words, frequencies)
        self.root = None

    def insert(self, word, frequency):
        if self.root is None:
            self.root = BSTNode(word, frequency)
        else:
            self._insert(self.root, word, frequency)

    def _insert(self, node, word, frequency):
        if node is None:
            return
        if frequency < node.frequency:
            if node.left is None:
                node.left = BSTNode(word, frequency)
            else:
                self._insert(node.left, word, frequency)
        else:
            if node.right is None:
                node.right = BSTNode(word, frequency)
            else:
                self._insert(node.right, word, frequency)

    def search(self, word, frequency):
        """Search for a word in the tree."""
        return self._search(self.root, word, frequency)

    def construct(self):
        for word, freq in zip(self.words, self.frequencies):
            self.insert(word, freq)

    def _search(self, node, word, frequency):
        """Helper function for search."""
        if node is None:
            return False
        if node.frequency == frequency:
            return True
        elif frequency < node.frequency:
            return self._search(node.left, word, frequency)
        else:
            return self._search(node.right, word, frequency)

    def inorder_traversal(self):
        """Perform an in-order traversal of the tree."""
        result = []
        self._inorder_traversal(self.root, result)
        return result

    def _inorder_traversal(self, node, result):
        """Helper function for in-order traversal."""
        if node:
            self._inorder_traversal(node.left, result)
            result.append((node.word, node.frequency))
            self._inorder_traversal(node.right, result)
