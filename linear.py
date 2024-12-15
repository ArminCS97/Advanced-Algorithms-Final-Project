from search import Search


class LinearSearch(Search):
    def __init__(self, words):
        super(LinearSearch, self).__init__(words, [])

    def search(self, word):
        for w in self.words:
            if w == word:
                return True
        return False

    def construct(self):
        pass
