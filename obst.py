class Search:
    def __init__(self, words, frequencies):
        self.words = words
        self.frequencies = frequencies

    def search(self, wor, *args, **kwargs):
        raise NotImplemented

    def construct(self):
        raise NotImplemented


class OBSTNode:
    def __init__(self, word):
        self.word = word
        self.left = None
        self.right = None


class OBSSearch(Search):
    """Class to construct and search in an Optimal Binary Search Tree."""
    def __init__(self, words, frequencies, dummy_frequencies):
        super().__init__(words, frequencies)
        self.dummy_frequencies = dummy_frequencies  # Dummy probabilities for unsuccessful searches
        self.n = len(words)  # Number of keys
        self.e = [[0] * (self.n + 1) for _ in range(self.n + 2)]  # Cost table
        self.w = [[0] * (self.n + 1) for _ in range(self.n + 2)]  # Weight table
        self.root = [[0] * (self.n + 1) for _ in range(self.n + 1)]  # Root table
        self.tree = None  # Root of the constructed OBST

    def construct(self):
        """Construct the Optimal Binary Search Tree using dynamic programming."""
        # Initialize base cases
        for i in range(1, self.n + 2):
            self.e[i][i - 1] = self.dummy_frequencies[i - 1]
            self.w[i][i - 1] = self.dummy_frequencies[i - 1]

        # Fill the tables using dynamic programming
        for l in range(1, self.n + 1):  # Length of the subproblem
            for i in range(1, self.n - l + 2):  # Start index
                j = i + l - 1  # End index
                self.e[i][j] = float('inf')  # Initialize to infinity
                self.w[i][j] = self.w[i][j - 1] + self.frequencies[j - 1] + self.dummy_frequencies[j]
                for r in range(i, j + 1):  # Possible roots
                    t = self.e[i][r - 1] + self.e[r + 1][j] + self.w[i][j]
                    if t < self.e[i][j]:
                        self.e[i][j] = t
                        self.root[i][j] = r

        # Build the tree from the root table
        self.tree = self._build_tree(1, self.n)

    def _build_tree(self, i, j):
        """Recursively build the OBST from the root table."""
        if i > j:
            return None
        r = self.root[i][j] - 1  # Convert 1-based index to 0-based
        node = OBSTNode(self.words[r])
        node.left = self._build_tree(i, r)
        node.right = self._build_tree(r + 2, j)
        return node

    def search(self, word, *args, **kwargs):
        """Search for a word in the constructed OBST."""
        return self._search(self.tree, word)

    def _search(self, node, word):
        """Recursive search in the OBST."""
        if node is None:
            return False
        if node.word == word:
            return True
        elif word < node.word:
            return self._search(node.left, word)
        else:
            return self._search(node.right, word)

    def inorder_traversal(self):
        """Perform an in-order traversal of the OBST."""
        result = []
        self._inorder_traversal(self.tree, result)
        return result

    def _inorder_traversal(self, node, result):
        """Helper for in-order traversal."""
        if node:
            self._inorder_traversal(node.left, result)
            result.append(node.word)
            self._inorder_traversal(node.right, result)
