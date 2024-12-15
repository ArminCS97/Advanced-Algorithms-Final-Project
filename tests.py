from bst_frequencies import BSTFrequencySearch
from bst_lexicographical import BSTLexicographicalSearch
from linear import LinearSearch
from obst import OBSSearch

words = ["elderberry", "apple", "banana", "date", "cherry"]
frequencies = [0.258, 0.194, 0.065, 0.129, 0.097]
dummy_frequencies = [0.032, 0.065, 0.032, 0.032, 0.032, 0.064]

assert sum(frequencies) + sum(dummy_frequencies) == 1

# Sort words, frequencies, and dummy_frequencies for
sorted_data = sorted(zip(words, frequencies))
sorted_words, sorted_frequencies = zip(*sorted_data)

# Convert back to lists
sorted_words = list(sorted_words)
sorted_frequencies = list(sorted_frequencies)

# dummy_frequencies remain the same since they correspond to boundaries
dummy_frequencies = dummy_frequencies

linear_search = LinearSearch(words)
bst_frequencies_search = BSTFrequencySearch(words=words, frequencies=frequencies)
bst_lexicographical_search = BSTLexicographicalSearch(words)
obst_search = OBSSearch(sorted_words, sorted_frequencies, dummy_frequencies)

linear_search.construct()
bst_frequencies_search.construct()
bst_lexicographical_search.construct()
obst_search.construct()

for word, freq in zip(sorted_words, sorted_frequencies):
    assert linear_search.search(word)
    assert bst_frequencies_search.search(word, freq)
    assert bst_lexicographical_search.search(word)
    assert obst_search.search(word)

for word, freq in zip(['Apple', 'Cherryyy'], [0.9, 0.99]):
    assert not linear_search.search(word)
    assert not bst_frequencies_search.search(word, freq)
    assert not bst_lexicographical_search.search(word)
    assert not obst_search.search(word)

assert bst_lexicographical_search.inorder_traversal() == ['apple', 'banana', 'cherry', 'date', 'elderberry']
assert bst_frequencies_search.inorder_traversal() == [
    ('banana', 0.065), ('cherry', 0.097), ('date', 0.129), ('apple', 0.194), ('elderberry', 0.258)
]
assert obst_search.inorder_traversal() == ['apple', 'banana', 'cherry', 'date', 'elderberry']
