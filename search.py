class Search:
    def __init__(self, words, frequencies):
        self.words = words
        self.frequencies = frequencies

    def search(self, wor, *args, **kwargs):
        raise NotImplemented

    def construct(self):
        raise NotImplemented
